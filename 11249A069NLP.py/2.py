from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_text="Hello Mr. Sanncy, have you watched *One Piece* yet? If not, you should definitely give it a try!"
words=word_tokenize(example_text)
stop_words = set(stopwords.words('english'))
filtered_sentence=[]
for w in words:
    if  w not in stop_words:
       filtered_sentence.append(w)
print(filtered_sentence)

