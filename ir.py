import csv
from bs4 import BeautifulSoup
import collections
import importlib
moduleName = 'hi_to_eng'
importlib.import_module(moduleName)
from hi_to_eng import transliterate,_setup
import re

def pharse_translate(query):
    li = []
    l = len(query.split(' '))
    temp = query.split(' ')
    for i in range(l):
        for j in range(l-1):
            for k in range(l):
                if k+i-j<l:
                    phrase = temp[k:k+i-j]
                    li.append(phrase)
    return li


f = open('/home/rishav/Desktop/hi-topics.txt', 'r')
read_file = f.read()

f = open('/home/rishav/Desktop/crowd_transliterations.hi-en.txt', 'r')
transliterate_file = f.read()

# with open('/home/rishav/Desktop/hi-en_dict.csv', 'r') as f_obj:
#     read_dict = csv.reader(f_obj)

trans_dict = {}
for line in transliterate_file.splitlines():
    # print(line)
    dict_list = re.split(r'\s{1,}', line)
    # print(dict_list)
    trans_dict.update({dict_list[1]: dict_list[0]})

# print(trans_dict['कोप'])

soup = BeautifulSoup(read_file, "html5lib")

titles = soup.find_all('title')
string = ""

for title in titles:
    if title is not None:
        string = string+'\n'+str(title)

queries = BeautifulSoup(string, "html5lib").text

dict = {}
with open('/home/rishav/Desktop/hi-en_dict.csv') as f_obj:
    reader = csv.DictReader(f_obj, delimiter=',')
    for line in reader:
        if line['hword'] in dict.keys():
            dict[line['hword']].append(line['eword'])
        else:
            dict.update({line['hword']: list([line['eword']])})

# print(dict['निराला'][0])
_setup()
# print(transliterate("निराला", 'devanagari', 'iast'))

eng_queries = ""
for query in queries.splitlines():
    eng_query = ""
    pharse = pharse_translate(query)
    word_list = query.split(' ')
    for p in phrase:
        if p in dict.keys():
            eng_query += dict[p]+' '
    
    for word in word_list:
        if (word in trans_dict) or (word in dict):
            if word in trans_dict:
                eng_query = eng_query+trans_dict[word]+' '
            if word in dict:
                if len(dict[word]) == 1:
                    eng_query = eng_query+dict[word][0]+' '
                else:
                    # for i in range(len(dict[word])):
                    eng_query = eng_query+dict[word][0]+' '
        else:
            eng_query = eng_query+(transliterate(word, 'devanagari', 'hk')).lower()+' '
    print(query)
    print(eng_query)
    eng_queries = eng_queries+eng_query+'\n'

f = open("/home/rishav/Desktop/expanded-queries.txt", "w+")
f.write("<topics>\n")
num = 76
for line in eng_queries.splitlines():
    f.write('\n<top>\n<num>'+str(num)+'</num>\n<title>'+line+'</title>\n</top>\n')
    num = num+1
f.write('</topics>\n')
f.close()





