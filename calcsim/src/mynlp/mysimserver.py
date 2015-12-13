#encoding=utf-8

'''
Created on 2015年12月13日

@author: luobu
'''
import os
from gensim import utils
import jieba
from simserver import SessionServer
from scipy.ndimage.filters import docdict
service = SessionServer('/tmp/my_server') # resume server (or create a new one)
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

corpus_path = '/Users/luobu/workspace/data/wechat/articles/2015-12-04'

corpus = []
for root, dirs, files in os.walk(corpus_path):
    for f in files[:10]:
        with open(os.path.join(root,f),'r') as fdoc:
            url = fdoc.readline()
            doc = fdoc.read()
            doc_cutted = list(jieba.cut(doc))
            docid = url.split('&')[3].split('=')[1]
        if len(doc)<1000:
            continue
        docdict = {}
        docdict['id'] = docid
        docdict['tokens'] = doc_cutted
        print docid
        print doc_cutted          
        corpus.append(docdict)
        
#===============================================================================
# 
# texts = ["Human machine interface for lab abc computer applications",
#          "A survey of user opinion of computer system response time",
#          "The EPS user interface management system",
#          "System and human system engineering testing of EPS",
#          "Relation of user perceived response time to error measurement",
#          "The generation of random binary unordered trees",
#          "The intersection graph of paths in trees",
#          "Graph minors IV Widths of trees and well quasi ordering",
#          "Graph minors A survey"]
# corpus = [{'id': 'doc_%i' % num, 'tokens': utils.simple_preprocess(text)}
#       for num, text in enumerate(texts)]
#===============================================================================
#service.train(corpus, method='lsi')
#service.index(corpus)
#print(service.find_similar('doc_0'))
