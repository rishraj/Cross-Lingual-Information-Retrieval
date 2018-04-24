from gensim.models import Word2Vec
import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import random


#shuffled word embeddings
#read parallel corpus for hindi
f_hindi = open('parallel/IITB.en-hi.hi', 'r')
lines_hindi = f_hindi.read().split("\n")
sentences_hindi = [line.split(' ') for line in lines_hindi]

#read parallel corpus for english
f_eng = open('parallel/IITB.en-hi.en', 'r')
lines_eng = f_eng.read().split("\n")
sentences_eng = [line.split(' ') for line in lines_eng]

#sentence by sentence shuffle merge
sentences_hi_en = []
for  i in range(len(lines_hindi)):
	temp = sentences_hindi[i]+sentences_eng[i]
	random.shuffle(temp)
	sentences_hi_en.append(temp)

#start training word vectors using gensim
print('Training word2vec ....')
model = Word2Vec(sentences_hi_en, min_count=1, size=300)
print('training done ...')

#saving the model
model.save('word2vec_merged_hi_en.bin')