import codecs
import nltk
from bs4 import BeautifulSoup

f = codecs.open("../data/testpage01.html", 'r', 'utf-8')
document = BeautifulSoup(f.read()).get_text()
[print(i) for i in document]



