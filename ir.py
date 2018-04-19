import csv
from bs4 import BeautifulSoup
import collections


f = open('/home/rishav/Desktop/hi-topics.txt', 'r')
read_file = f.read()

# with open('/home/rishav/Desktop/hi-en_dict.csv', 'r') as f_obj:
#     read_dict = csv.reader(f_obj)



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
            dict.update({line['hword']: list(line['eword'])})

# print(dict)

eng_queries = ""
for query in queries.splitlines():
    eng_query = ""
    word_list = query.split(' ')
    # print(wordlist)
    for word in word_list:
        if word in dict:
            # eng_query = eng_query+'('+word+')'+dict[word]+' '
            eng_query = eng_query+dict[word]+' '
            # print(word, ' ', dict[word],' ')
    print(query)
    print(eng_query)
    eng_queries = eng_queries+eng_query+'\n'

f = open("/home/rishav/Desktop/en-queries.txt", "w+")
f.write("<topics>\n")
num = 76
for line in eng_queries.splitlines():
    f.write('\n<top>\n<num>'+str(num)+'</num>\n<title>'+line+'</title>\n</top>\n')
    num = num+1
f.write('</topics>\n')
f.close()





