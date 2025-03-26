import nltk
from nltk.tokenize import sent_tokenize

paragraf1 = "Naso goreng anti kecap"
paragraf2 = "Mobilelegend bang bangggg"
kalimat = "m untuk mulyono."

sentences1 = sent_tokenize(kalimat)
sentences2 = sent_tokenize(paragraf1)
sentences3 = sent_tokenize(paragraf2)


print("Tokenized Sentences 1:", sentences1)
print("Tokenized Sentences 2:", sentences2)
print("Tokenized Sentences 3:", sentences3)