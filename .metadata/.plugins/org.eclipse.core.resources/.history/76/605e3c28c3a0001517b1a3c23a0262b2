'''
Created on 2015年12月1日

@author: luobu
'''
#encoding=utf-8
import os
from gensim import corpora, models, similarities
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.stem.lancaster import LancasterStemmer
import jieba
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MyCorpus(object):
    def __iter__(self):
        for line in open('mycorpus.txt'):
        # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())