from gensim import corpora, models, similarities
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
documents = ["Shipment of gold damaged in a fire",\
             "Delivery of silver arrived in a silver truck",\
             "Shipment of gold arrived in a truck"]
texts = [[word for word in document.lower().split()] for document in documents]
print texts
dictionary = corpora.Dictionary(texts)
print dictionary.token2id
corpus = [dictionary.doc2bow(text) for text in texts]
print corpus
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print doc
print tfidf.dfs
lsi = models.LsiModel(corpus_tfidf,id2word=dictionary,num_topics=2)
lsi.print_topics(2)
corpus_lsi = lsi[corpus_tfidf]
for doc in corpus_lsi:
    print doc
lda = models.LdaModel(corpus_tfidf,id2word=dictionary,num_topics=2)
lda.print_topics(2)