import codecs
import nltk
nltk.download('punkt')
import operator

from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.probability import ConditionalFreqDist

#from matplotlib import pylab

def docFromFile(path):
   f = codecs.open(path, 'r', 'utf-8')
   return BeautifulSoup(f.read()).get_text()


def getTokenFrequenciesFromDoc(document):
   tokens = word_tokenize(document)
   print(len(tokens))
   wordList=list(set(tokens))

   tokeFreqs=dict.fromkeys(wordList,0)
   for word in tokens:
      tokeFreqs[word]+=1
   return (sorted(tokeFreqs.items(), key=operator.itemgetter(1),reverse=True))



