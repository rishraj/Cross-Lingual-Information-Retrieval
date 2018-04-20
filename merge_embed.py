from gensim.models import Word2Vec
import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import random


#shuffled word embeddings
f_hindi = open('parallel/IITB.en-hi.hi', 'r')
lines_hindi = f_hindi.read().split("\n")
sentences_hindi = [line.split(' ') for line in lines_hindi]

f_eng = open('parallel/IITB.en-hi.en', 'r')
lines_eng = f_eng.read().split("\n")
sentences_eng = [line.split(' ') for line in lines_eng]


sentences_hi_en = []
for  i in range(len(lines_hindi)):
	temp = sentences_hindi[i]+sentences_eng[i]
	random.shuffle(temp)
	sentences_hi_en.append(temp)

#print(len(lines_hindi),len(lines_eng))
print(sentences_hi_en[:10])
print('Training word2vec ....')
model = Word2Vec(sentences_hi_en, min_count=1, size=300)
print('training done ...')
model.save('zword2vec_merged_hi_en.bin')