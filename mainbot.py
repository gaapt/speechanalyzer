import nltk
from nltk import word_tokenize, FreqDist
import matplotlib


#opens our text file
raw = open('obamaspeech').read()
#print raw

#formats then tokenizes
tokens = word_tokenize(raw.decode('utf-8'))
#print tokens


#puts part of speech tags in tokens
tagged = nltk.pos_tag(tokens)
#print tagged


#outputs list w tags
len_tagged = len(tagged)
tag='a'
i=0
while i< len_tagged:
	tag= tag+' ' +tagged[i][1]
	i = i + 1
#print tag


#proceeds with plotting
fd_tag = nltk.FreqDist(tag for (word,tag) in tagged)
fd_tag.plot()