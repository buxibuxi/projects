'''
Created on 2015年12月1日

@author: luobu
'''

#encoding=utf-8

'''
Created on 2015年12月2日

@author: luobu
'''

import os
from gensim import corpora, models, similarities
import logging
import jieba
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 


class MyCorpus(object):
    '''
    classdocs
    '''


    def __init__(self, corpus_path):
        self.cn_stopwords = []
        with open('/Users/luobu/workspace/python/token/src/cn_stopwords.txt') as f:
            for line in f.readlines():
                self.cn_stopwords.append(line.strip().decode('utf-8'))
        self.__gendict__(corpus_path)
        self.__gencorpus__()
            
    def __gendict__(self,corpus_path):
        self.doc_list = []
        self.doc_list1 = []
        self.file_list = []
        for root, dirs, files in os.walk(corpus_path):
            for f in files:
                with open(os.path.join(root,f),'r') as fdoc:
                    doc = fdoc.read()
                if len(doc)<1000:
                    continue
                self.file_list.append(f)
                doc_cutted = jieba.cut(doc)
                
                doc1 = list(jieba.cut(doc))
                self.doc_list.append(doc_cutted)
                self.doc_list1.append(doc1)
        self.dictionary = corpora.Dictionary(self.doc_list)      
        stop_ids = [self.dictionary.token2id[stopword] for stopword in self.cn_stopwords \
                     if stopword in self.dictionary.token2id]
        once_ids = [tokenid for tokenid, docfreq in self.dictionary.dfs.iteritems() if docfreq == 1]
            
        self.dictionary.filter_tokens(stop_ids+once_ids)
        self.dictionary.compactify()
        #print self.dictionary

        #self.dictionary = corpora.Dictionary(line.lower().split() for line in open('mycorpus.txt'))
    def __gencorpus__(self):
        self.corpus = (self.dictionary.doc2bow(doc) for doc in self.doc_list1)
    #===========================================================================
    # def __iter__(self):
    #     for doc in self.doc_list1:
    #         yield self.dictionary.doc2bow(doc)
    #             
    #===========================================================================

corpus_path ='/Users/luobu/workspace/python/scrapy/wechat/wechat/articles/2015-12-04'
M = MyCorpus(corpus_path)
mycorpus0 = M.corpus
corpora.MmCorpus.serialize('/tmp/corpus.mm', mycorpus0)
mycorpus = corpora.MmCorpus('/tmp/corpus.mm')
#for i in mycorpus:
#    print i
#print M.dictionary
tfidf = models.TfidfModel(mycorpus)
mycorpus_tfidf = tfidf[mycorpus]
lsi = models.LsiModel(mycorpus_tfidf, id2word=M.dictionary, num_topics=400)
index = similarities.MatrixSimilarity(lsi[mycorpus]) 
#===============================================================================
# ml_course = M.doc_list1[1]
# print ml_course
# ml_bow = M.dictionary.doc2bow(ml_course)
# ml_lsi = lsi[ml_bow]
# print ml_lsi
#===============================================================================
#sims = index[ml_lsi]
#sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
#print sort_sims
#for c in sort_sims:
#    print c,M.doc_list1[c[0]]


print '**********'
i=0
thres = 0.90
simdict = {}
for item in index:
    for j in range(i+1,len(item)):
        if item[j]>thres:
            simdict[(i,j)] = item[j]
    i +=1
print len(simdict)
sort_sims = sorted(simdict.iteritems(), key=lambda item: item[1],reverse=True)
for i in sort_sims[:10]:
    print i
for item in sort_sims[:1000]:
    a = item[0][0]
    b = item[0][1]
    sim = item[1]
    print M.file_list[a]
#    print M.doc_list1[a]
#    print M.dictionary.doc2bow(M.doc_list1[a])
    print M.file_list[b]
#    print M.doc_list1[b]
#    print M.dictionary.doc2bow(M.doc_list1[b])    
    print sim
    print '****************************'
print len(simdict)
            
    