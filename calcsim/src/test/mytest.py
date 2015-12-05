'''
Created on 2015年12月1日

@author: luobu
'''

if __name__ == '__main__':
    pass

dictionary = corpora.Dictionary(line.lower().split() for line in open('mycorpus.txt'))
>>> # remove stop words and words that appear only once
>>> stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
>>>             if stopword in dictionary.token2id]
>>> once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
>>> dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
>>> dictionary.compactify() # remove gaps in id sequence after words that were removed
>>> print(dictionary)
Dictionary(12 unique tokens)