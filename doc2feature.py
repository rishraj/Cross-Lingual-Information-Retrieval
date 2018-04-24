import numpy as np
import os
from gensim.models import Word2Vec
import re
from bs4 import BeautifulSoup
import sys

if len(sys.argv) != 3:
	# print(sys.argv[0], sys.argv[1], sys.argv[2])
	print('Usage: python doc2feature path_of_documents path_of_embedding')
	sys.exit(1)

# directory = 'dataset/'
directory = sys.argv[1]
# for filename in os.listdir(directory):
# 	if filename.endswith('.utf8'):

# model_en = Word2Vec.load('model/word2vec-eng.bin')
model_en = Word2Vec.load(sys.argv[2])
fd = open('feature.txt', 'w')

f = open('collection.spec', 'r')
lines = f.read().splitlines()
print(len(lines))

for file in lines:
    # print (os.path.join(path, name))
    # print(name)
    f = open(file, 'r')
    st = f.read()
    f.close()
    soup = BeautifulSoup(st)
    t = soup.find_all('text')
    te = (str(t).replace('\n', ' ')).split(' ')
    text = [t for t in te if t!='']
    text = text[1:-1]
    if len(text) == 0:
    	continue
    vec = np.zeros(300)
    for item in text:
    	try:
    		vec += np.array(model_en[item])
    	except:
    		continue
    feature = vec/len(text)
    # feature = feature.reshape((1,300))
    feat = ', '.join(map(str, feature.tolist()))

    string = str(file) + ', ' + feat + '\n'
    # print(string)
    fd.write(string)
    	
    

