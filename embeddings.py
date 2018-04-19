from gensim.models import Word2Vec
import csv
import numpy as np
from sklearn.linear_model import LinearRegression

# fd = open('parallel/IITB.en-hi.hi', 'r')
# lines = fd.read().splitlines()
# sentences = [line.split(' ') for line in lines]
# print(sentences[:10])
# print('Training word2vec ....')
# model = Word2Vec(sentences, min_count=2, size=300)
# print('training done ...')
# model.save('model/word2vec-hi.bin')
# print(len(model))
model_en = Word2Vec.load('model/word2vec-eng.bin')
model_hi = Word2Vec.load('model/word2vec-hi.bin')
words = list(model_hi.wv.vocab)
# print(len(words))
# # print((model['स्थिति']))
# sim = model_hi.wv.similar_by_vector(model_hi['मंदिर'], topn=10, restrict_vocab=None)
# print(sim)

dictionary = []
with open('English-Hindi Dictionary.csv') as csvfile:
	file = csv.reader(csvfile)
	for row in file:
		if row[0]=='eword' and row[1]=='hword':
			continue
		if row[0]!='' and row[1]!='':
			dictionary.append([row[0], row[1]])

print('Dictionary loaded ...')

hindi = np.zeros((len(dictionary),300))
english = np.zeros((len(dictionary),300))

# print(dictionary[0])
i = 0
for d in dictionary:
	tmp = np.zeros(300)
	temp = d[1].split(' ')
	li = [x for x in temp if x!='']
	# print(li)
	if li==[]:
		continue
	# print(li)
	for item in li:
		try:
			tmp += np.array(model_hi[item])
		except:
			continue
	# print(type(hindi[i]), type(tmp))
	hindi[i] = tmp/len(li)

	tmp = np.zeros(300)
	temp = d[0].split(' ')
	li = [x for x in temp if x!='']
	# print(li)
	if li==[]:
		continue
	for item in li:
		try:
			tmp += np.array(model_en[item])
		except:
			continue
	english[i] = tmp/len(li)
	i += 1

hindi = hindi[:i]
english = english[:i]

print(hindi.shape, english.shape, i)
# print(len(hindi[np.nonzero(hindi)]))


regr = LinearRegression()
regr.fit(hindi, english)

hi = model_hi['विवाद'].reshape(1,-1)
en = regr.predict(hi)
print(en.shape, type(en), type(model_hi['मंदिर']), model_hi['मंदिर'].shape)
sim = model_en.wv.similar_by_vector(en.reshape(300,), topn=10, restrict_vocab=None)
print(sim)