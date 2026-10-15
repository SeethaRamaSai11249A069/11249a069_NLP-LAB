from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 
ps = PorterStemmer()
new_text= "Is is very important to be pythonly while you are pythoning with python.all pythoner have poorly pythoned atleast once"
words = word_tokenize(new_text)
for w in words:
 print(ps.stem(w))
