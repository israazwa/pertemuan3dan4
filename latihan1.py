import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

nltk.download('punkt')

kalimat = "Makan siang bergizi gratis."

tokens = word_tokenize(kalimat)

print("Tokenized Words:", tokens)