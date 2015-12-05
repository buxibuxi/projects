#encoding=utf-8

import os
from gensim import corpora, models, similarities
import logging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.stem.lancaster import LancasterStemmer
import jieba
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
st = LancasterStemmer()


fpath = '/Users/luobu/workspace/python/scrapy/wechat/wechat/articles/2015-11-12'
fname = os.path.join(fpath,'vivo智能手机_2015-11-11_vivo&维密｜维密20周年大秀，除了看身材还有这些“内幕”！')
cn_stopwords = []
with open('/Users/luobu/workspace/python/token/src/cn_stopwords.txt') as f:
    for line in f.readlines():
        cn_stopwords.append(line.strip().decode('utf-8'))
print cn_stopwords
seg_list = []
for root,dirs,files in os.walk(fpath):
    for f in files:
        fname = os.path.join(root,f)
        with open(fname,'r') as farticle:
            article = farticle.read()
            seg_list.append(jieba.cut(article))
print type(seg_list)
#seg_list_filterd = [word for word in seg_list if not word in cn_stopwords]
dictionary = corpora.Dictionary(seg_list)
#dictionary_filted = corpora.Dictionary([seg_list_filterd,seg_list_filterd])
ft = file('test.txt','wb')
ft1 = file('test1.txt','wb')
for key in dictionary.token2id:
    ft.write(key+'\r\n')
stop_ids = [dictionary.token2id[stopword] for stopword in cn_stopwords  if stopword in dictionary.token2id]
dictionary.filter_tokens(stop_ids)
dictionary.compactify()
for key in dictionary.token2id:
    ft1.write(key+'\r\n')
ft.close()
ft1.close()
corpus = dictionary.doc2bow(seg_list)
print corpus
