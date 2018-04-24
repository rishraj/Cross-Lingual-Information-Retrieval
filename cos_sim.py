import numpy as np

# def cos_sim(a,b):
# 	d = a*b
# 	d = d.sum(axis = 1)
# 	norm1 = np.linalg.norm(a, axis = 1)
# 	norm2 = np.linalg.norm(b)
# 	sim = -d/(norm1*norm2)
# 	return np.argsort(sim)

def cos_sim(a,b):
	li = []
	for i in range(a.shape[0]):
		d = np.dot(a[i], b)
		norm1 = np.linalg.norm(a[i])
		norm2 = np.linalg.norm(b)
		sim = -d/(norm1*norm2)
		li.append(sim)
	return np.argsort(np.array(li))


def read_doc_vec(fname):
	doc_name = []
	doc_feature = np.zeros((125517,300))
	f = open (fname, 'r')
	data = f.read().split("\n")
	print(len(data))
	k = 0
	for line in data:
		if line == '':
			continue
		temp = line.split(", ")
		doc_name.append(temp[0])
		t = [float(i) for i in temp[1:]]
		# print(len(t))
		# print(np.array(t).shape)
		doc_feature[k] = np.array(t)
		k += 1
	# print(len(doc_feature[0]))
	return doc_name, doc_feature


def read_query_vec(fname):
	doc_name = []
	doc_feature = np.zeros((50,300))
	f = open (fname, 'r')
	data = f.read().split("\n")
	print(len(data))
	k = 0
	for line in data:
		if line == '':
			continue
		temp = line.split(", ")
		doc_name.append(temp[0])
		t = [float(i) for i in temp[1:]]
		# print(len(t))
		# print(np.array(t).shape)
		doc_feature[k] = np.array(t)
		k += 1
	# print(len(doc_feature[0]))
	return doc_name, doc_feature

query_fname, query_feature = read_query_vec("query-feature.txt")
doc_fname, doc_feature = read_doc_vec("feature.txt")

print((doc_feature).shape)
print(np.array(doc_feature).shape)
print(doc_feature.shape, query_feature.shape)

f = open("result1.txt", "w+")

for i in range(len(query_fname)):
	arg = cos_sim(doc_feature,query_feature[i])
	for j in range(1000):
		f.write(query_fname[i]+ " " + doc_fname[arg[j]] + '\n')

f.close()