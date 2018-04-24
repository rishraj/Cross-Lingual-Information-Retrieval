import numpy as np

def cos_sim(a,b):
	d = a*b
	d = d.sum(axis = 1)
	norm1 = np.linalg.norm(a, axis = 1)
	norm2 = np.linalg.norm(b)
	sim = d/(norm1*norm2)
	return np.argsort(sim)

def read_doc_vec(fname):
	doc_name = []
	doc_feature = []
	with open (fname, 'r') as f:
		data = f.read().split("\n")
	for line in data:
		temp = line.split(", ")
		doc_name.append(temp[0])
		t = [float(i) for i in temp[1:]]
		doc_feature.append(t)
	return doc_name, np.array(doc_feature)

query_fname, query_feature = read_doc_vec("query-feature.txt")
doc_fname, doc_feature = read_doc_vec("feature.txt")

f = open("result.txt", "w+")

for i in range(len(query_fname)):
	arg = cos_sim(doc_feature,query_feature[i])
	for j in range(1000):
		f.write(query_fname[i]+ " " + doc_name[arg[j]])

f.close()