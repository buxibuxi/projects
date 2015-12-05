

class MyCorpus():
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        for i in range(self.n):
            # assume there's one document per line, tokens separated by whitespace
            yield i+1
            
f = MyCorpus(9)
print f 
for i in f:
    print i

