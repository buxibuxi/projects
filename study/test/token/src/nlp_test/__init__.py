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

coursera = '/Users/luobu/workspace/python/nlp/data/coursera_corpus'
courses = [line.strip() for line in file(coursera)]
courses_name = [course.split('\t')[0] for course in courses]
#print courses_name[0:10]
texts_lower = [[word for word in document.lower().split()] for document in courses]
#print texts_lower[0]
texts_tokenized = [[word.lower() for word in word_tokenize(document.decode('utf-8'))] \
                   for document in courses]
#print texts_tokenized[0]
e_stop = stopwords.words('english')
e_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
#print e_stop
#text_filtered = [[word for word in document \
#                            if not word in e_stop and not word in e_punctuations] \
#                           for document in texts_tokenized]
#text_stemmed = [[st.stem(word) for word in document] for document in text_filtered]
#print text_stemmed
#all_stem = sum(text_stemmed,[])
#stems_once = set(stem for stem in set(all_stem) if all_stem.count(stem) ==1)
#texts = [[stem for stem in text if stem not in stems_once] for text in text_stemmed]
#dictionary = corpora.Dictionary(texts)
#corpus = [dictionary.doc2bow(text) for text in texts]
#tfidf = models.TfidfModel(corpus)
#corpus_tfidf = tfidf[corpus]
#lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
#index = similarities.MatrixSimilarity(lsi[corpus])

#print courses_name[210]
#ml_course = texts[210]
#ml_bow = dictionary.doc2bow(ml_course)



fpath = '/Users/luobu/workspace/python/scrapy/wechat/wechat/articles/2015-11-20'
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
print dictionary
for key in dictionary.token2id:
    ft1.write(key+'\r\n')
ft.close()
ft1.close()
#corpus = dictionary.doc2bow(seg_list)
#print corpus
