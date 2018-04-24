from gensim.models import Word2Vec
import csv
import sys
import numpy as np
from sklearn.linear_model import LinearRegression
import random


def main(hindi_file,english_file):
	#shuffled word embeddings
	#read parallel corpus for hindi
	f_hindi = open(hindi_file, 'r')
	lines_hindi = f_hindi.read().split("\n")
	sentences_hindi = [line.split(' ') for line in lines_hindi]	

	#read parallel corpus for english
	f_eng = open(english_file, 'r')
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

if __name__ == '__main__':
	if len(sys.argv) != 3:
		# print(sys.argv[0], sys.argv[1], sys.argv[2])
		print('Usage: python merge_embed.py <Parallel corpus Hindi file> <Parallel corpus English file>')
		sys.exit(1)
	main(sys.argv[1],sys.argv[2])
