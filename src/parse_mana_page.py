import codecs
import nltk

#we'll be using the punkt sentence tokenizer
nltk.download('punkt')
import string
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

from bs4 import BeautifulSoup

#unused imports from dev experimenting
#from nltk import word_tokenize
#from nltk.probability import ConditionalFreqDist

#from matplotlib import pylab
#import operator



#this is the tokenizer method used by the TfidfVectorizer
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems


#opens an exported Mana file and uses BeautifulSoup to parse it
def docFromFile(path):
   f = codecs.open(path, 'r', 'utf-8')
   return BeautifulSoup(f.read()).getText()


def getTokenFrequenciesFromPath(path,stringToTest):
    #based of TF-IDF example from https://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
    #RENAME FUNCTION- function now does matching
   #add options for English default, removing punctuation and stopwords, and installing a cleaning pipeline
   token_dict = {}
   for dirpath, dirs, files in os.walk(path):
       for f in files:
           fname = os.path.join(dirpath, f)
           print ("filename=", fname)
           with open(fname) as pearl:
               text=docFromFile(fname)
               #text2 = pearl.read()  --using the BeautifulSoup parsing insted
               token_dict[f] = text.lower().translate(string.punctuation)
               #tfidfPerFile = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
               #tfidf_per_file[fname]=tfidfPerFile.fit_transform(token_dict[f])

   tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
   tfs = tfidf.fit_transform(token_dict.values())
#   print ("Features:"+ str(tfidf.get_feature_names().__len__()))
   print ("Features: "+str(tfidf.get_feature_names()))
   print ("Shape:" + str(tfs.shape))

   #str = 'new hires of Mozilla culture experiment Portland'  #string of words to compareto- MAKE THIS A PARAMETER
   response = tfidf.transform([stringToTest])
   print ("response of transformation")
   print (response)

   feature_names = tfidf.get_feature_names()
   for col in response.nonzero()[1]:
       print (feature_names[col], ' - ', response[0, col])


    #feature_names_per_file=

   #my initial dictionary work is below

   #tokens = word_tokenize(document)
   #print(len(tokens))
   #wordList=list(set(tokens))

   #tokeFreqs=dict.fromkeys(wordList,0)
   #for word in tokens:
    #  tokeFreqs[word]+=1
   #return (sorted(tokeFreqs.items(), key=operator.itemgetter(1),reverse=True))

#tf/df- term frequency divided by document frequency


