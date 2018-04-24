import csv
from bs4 import BeautifulSoup
import collections
import importlib
moduleName = 'hi_to_eng'
importlib.import_module(moduleName)
from hi_to_eng import transliterate,_setup
import re
from gensim.models import Word2Vec
import numpy as np
import random

#read hindi query file
f = open('hi.topics.76-125.2010.txt', 'r')
read_file = f.read()

#read transliteration dictionary
f = open('crowd_transliterations.hi-en.txt', 'r')
transliterate_file = f.read()


#create in memory representation for transliteration dictionary
trans_dict = {}
for line in transliterate_file.splitlines():
    dict_list = re.split(r'\s{1,}', line)
    trans_dict.update({dict_list[1]: dict_list[0]})


#to parse the query and find title field
soup = BeautifulSoup(read_file, "html5lib")

titles = soup.find_all('title')
string = ""

for title in titles:
    if title is not None:
        string = string+'\n'+str(title)

queries = BeautifulSoup(string, "html5lib").text

dict = {}
max_phrase_len = 0

#read bilingual hindi english dictionary and create in memory representation
with open('English-Hindi Dictionary.csv') as f_obj:
    reader = csv.DictReader(f_obj, delimiter=',')
    for line in reader:
        if line['hword'] in dict.keys():
            dict[line['hword']].append(line['eword'])
        else:
            dict.update({line['hword']: list([line['eword']])})

#to run transliteration module setup is done 
_setup()
# print(transliterate("निराला", 'devanagari', 'hk'))

#load word vectors
model_hi_en = Word2Vec.load('word2vec_merged_hi_en.bin')
vocab = list(model_hi_en.wv.vocab)

#to remove punctuation mark set rem_punc to 1
rem_punc = 0
punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#to select top k set top_k to k
top_k = 2

eng_queries = ""
for query in queries.splitlines():
    eng_query = ""
    no_punct = ""  
    for char in query:  
        if rem_punc and char not in punctuation:  
            no_punct = no_punct + char 
    if rem_punc:
    	word_list = no_punct.split(' ')
    else:
    	word_list = query.split(' ')

    for word in word_list:
        if (word in trans_dict) or (word in dict):
            if word in trans_dict:
                eng_query = eng_query+trans_dict[word]+' '
            if word in dict:
                if len(dict[word]) == 1:
                    eng_query = eng_query+dict[word][0]+' '
                else:
                    if word in vocab:
                        cos_sim = []
                        for w in dict[word]:
                            if w in vocab:
                                sim = model_hi_en.similarity(word,w)
                            else:
                                sim = -1
                            cos_sim.append(sim)
                        l = np.array(cos_sim)
                        max_sims = (-l).argsort()
                        s = ""
                        if len(cos_sim)>=top_k:
                            for i in range(top_k):
                                s = s+ dict[word][max_sims[i]] + " "
                        else:
                            for i in range(len(cos_sim)):
                                s = s + dict[word][i] + " "
                        eng_query = eng_query+s+' '
                    else:
                        temp = dict[word]
                        random.shuffle(temp)                        
                        s = ""
                        if len(temp)>=top_k:
                            for i in range(top_k):
                                s = s+ temp[i] + " "
                        else:
                            for i in range(len(temp)):
                                s = s + temp[i] + " "
                        eng_query = eng_query+s+' '

        else:
            eng_query = eng_query+(transliterate(word, 'devanagari', 'hk')).lower()+' '
    print(query)
    print(eng_query)
    eng_queries = eng_queries+eng_query+'\n'

#write query in the file
f = open("merged_embed_dict_en-queries_top2sim_nopunc.txt", "w+")
f.write("<topics>\n")

#format the English query
num = 76
for line in eng_queries.splitlines():
    f.write('\n<top>\n<num>'+str(num)+'</num>\n<title>'+line+'</title>\n</top>\n')
    num = num+1
f.write('</topics>\n')
f.close()





