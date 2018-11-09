import codecs
import nltk
nltk.download('punkt')

from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.probability import ConditionalFreqDist

#from matplotlib import pylab

f = codecs.open("../data/testpage01.html", 'r', 'utf-8')
document = BeautifulSoup(f.read()).get_text()
#[print(i) for i in document]

tokens = word_tokenize(document)
print(len(tokens))
wordList=list(set(tokens))

tokeFreqs=dict.fromkeys(wordList,0)
for word in tokens:
   tokeFreqs[word]+=1
print (tokeFreqs)


