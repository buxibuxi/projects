#encoding=utf-8

'''
Created on 2015年12月12日

@author: luobu
'''

import redis
import os
import csv
from mynlp import mycorpus
import logging
import time
from scipy.stats._continuous_distns import loggamma
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                     datefmt='%a, %d %b %Y %H:%M:%S',
                     filename = '../../log/WeCheat.log',
                     level=logging.INFO) 

class WeCheat(object):
    '''
    classdocs
    '''
    def __init__(self, docspath,corpus_path,dic_path):
        '''
        Constructor
        '''
        self.r = redis.Redis(db=2)
        self.p = self.r.pipeline()
        self.docspath = docspath
        self.redisdocs = 'docs' #包含所有文章id的集合 
        self.cheatsrc = 'cheatsrc'
        self.cheatset = 'cheatset'       
        self.corpus_path = corpus_path
        self.dic_path = dic_path
    def calccheatdocs(self):
        self.CC = mycorpus.MyCorpus(self.corpus_path,self.dic_path)
        cheatpairs = self.CC.gensim()
        for (doc1,doc2) in cheatpairs:
            if not self.__cheatsame__(doc1, doc2):
                self.__cheatunion__(doc1, doc2)
    def __updatecheatdoc__(self,oldsrc,newsrc):
        newcheatset = newsrc + self.cheatset
        oldcheatset = oldsrc + self.cheatset
        self.r.sadd(newcheatset,oldsrc)
        self.r.sadd(self.cheatsrc,newsrc)         
        if self.r.sismember(self.cheatsrc,oldsrc):
            for docid in self.r.smembers(oldsrc+self.cheatset):
                self.r.sadd(newcheatset,docid)
            self.r.delete(oldcheatset)
            self.r.srem(self.cheatsrc,oldsrc)        
    def __cheatunion__(self,doc1,doc2):
        #合并两篇有抄袭关系的文章所在的集合
        src1 = self.__getsrc__(doc1)
        src2 = self.__getsrc__(doc2)
        if src1!=src2:
            pt1 = time.mktime(time.strptime(self.r.hget(src1,'ptime'),"%Y-%m-%d %H:%M:%S"))
            pt2 = time.mktime(time.strptime(self.r.hget(src2,'ptime'),"%Y-%m-%d %H:%M:%S"))
            if pt1<pt2:
                self.r.hset(src2,'src',src1)
                self.__updatecheatdoc__(src2, src1)
            else:
                self.r.hset(src1,'src',src2)
                self.__updatecheatdoc__(src1, src2)
            
            
    def __cheatsame__(self,doc1,doc2):
        #判断两篇有抄袭关系的文章是否已经属于同一个集合
        try:
            return self.r.hget(doc1,'src') == self.r.hget(doc2,'src')
        except Exception,e:
            logging.info(Exception)
            logging.info(e)
            logging.info(doc1+'_'+doc2)
        
    def __getsrc__(self,doc):
        docid = doc
        while docid != self.r.hget(docid,'src'):
            docid = self.r.hget(docid,'src')
        return docid
       
    def save_basicinfo(self):
        for root,dirs,files in os.walk(self.docspath):
            for f in files:
                if os.path.splitext(f)[1]!= '.csv':
                    continue
                linkfile = os.path.join(root,f)
                with open(linkfile,'rb') as csvfile:
                    reader = csv.reader(csvfile)
                    num = 0
                    for line in reader:
                        tdict = {}
                        num = num +1
                        if num <= 2:
                            continue
                        url = line[3]
                        docid = url.split('&')[3].split('=')[1]
                        tdict['acntname'] = line[0]
                        tdict['acntid'] = line[1]
                        tdict['title'] = line[2]
                        tdict['url'] = url 
                        tdict['ptime'] = line[4]
                        tdict['readnum'] = line[5]
                        tdict['praznum'] = line[6]
                        tdict['isori'] = line[12] 
                        tdict['src'] = docid
                        tdict['srcmark'] = ""
                        self.p.hmset(docid,tdict)
                        self.p.sadd(self.redisdocs,docid)
                #os.rename(linkfile,linkfile+'.done')
        self.p.execute()
                        
        
                        
                        
                        