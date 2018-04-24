import numpy as np
import os
from gensim.models import Word2Vec
import re
from bs4 import BeautifulSoup
import sys

if len(sys.argv) != 3:
	# print(sys.argv[0], sys.argv[1], sys.argv[2])
	print('Usage: python doc2feature path_of_queryfile path_of_embedding')
	sys.exit(1)

# model_hi = Word2Vec.load('../hi/hi.bin')
model_hi = Word2Vec.load(sys.argv[2])
fd = open('query-feature.txt', 'w')

# f = open('queries-modified.txt', 'r')
f = open(sys.argv[1])
st = f.read()
f.close()
soup = BeautifulSoup(st, "html5lib")

titles = soup.find_all('title')
string = ""


for title in titles:
    if title is not None:
        string = string+'\n'+str(title)

queries = BeautifulSoup(string, "html5lib").text

query = queries.split('\n')
num = 76

for i in query:
	vec = np.zeros(300)

	for item in i:
		try:
			vec += np.array(model_hi[item])
		except:
			continue

	feature = vec/len(i)
	feat = ', '.join(map(str, feature.tolist()))

	string = str(num) + ', ' + feat + '\n'
	# print(string)
	num += 1
	fd.write(string)