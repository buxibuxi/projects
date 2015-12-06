import os
from gensim import corpora, models, similarities
import logging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.stem.lancaster import LancasterStemmer

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
text_filtered = [[word for word in document \
                            if not word in e_stop and not word in e_punctuations] \
                           for document in texts_tokenized]
text_stemmed = [[st.stem(word) for word in document] for document in text_filtered]
print text_stemmed
all_stem = sum(text_stemmed,[])
stems_once = set(stem for stem in set(all_stem) if all_stem.count(stem) ==1)
texts = [[stem for stem in text if stem not in stems_once] for text in text_stemmed]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
index = similarities.MatrixSimilarity(lsi[corpus])

print courses_name[210]
ml_course = texts[210]
ml_bow = dictionary.doc2bow(ml_course)
ml_lsi = lsi[ml_bow]
print ml_lsi
sims = index[ml_lsi]
sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
print sort_sims[0:10]
for c in sort_sims[:5]:
    print c,courses[c[0]]

#print brown.readme()
#print len(brown.words())
