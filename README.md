**Project Report** has been added as *Project_Report.pdf*

The queries are assumed to be given in Hindi and converted to English

Python files:
---------------------------
cos_sim.py: It takes two files containing the feature vectors of all documents and queries and retrieves 1000 docs for each query and saves it in file 'result1.txt'.

doc2feature.py: It takes the embeddings for English words and saves feature vectors for all documents to file 'feature.txt'.

embeddings.py: It takes embeddings of English and Hindi words as well as Hindi-English Dictionary, and saves translated queries in 'expanded-queries.txt'. 

query2feature.py: It takes embeddings of Hindi words and queries file. It saves the feature vectors of each queries in 'query-feature.txt'. 

hi_to_eng.py : Used for transliteration. It takes Hindi word and script of the word (i.e. Devanagiri(devanagiri)) and script of the output word (i.e Roman(roman), Harvard-kyoto(hk)) and generates the transliterate word.

ir.py : It chooses any random English word from the list of candidate words available in the dictionary. This method was opted to form a baseline which we could use to compare the performance of other methods

ir_cos_sim.py : It takes four file as command line argument Hindi query file,  transliteration dictionary, import sys, word2vec word embeddings and generate a English query file(english_queries.txt). It is for the dictinary based approach with cosine similarity to remove the ambiguity. **(Best results obtained)**
e.g. python ir_cos_sim.py hi.topics.76-125.2010.txt crowd_transliterations.hi-en.txt English-Hindi_Dictionary.csv word2vec_merged_hi_en.bin 


merged_embed.py : It takes two file as command line argument one is parallel corpus for Hindi and the other is parallel corpus for English and generates merged word embeddings, that is by merging two sentence (one from Hindi and the other from English) and then using gensim to generate word2vec for words.
e.g. python merge_embed.py parallel/IITB.en-hi.hi parallel/IITB.en-hi.en 

Dataset Links -

Queries - http://arnab.cse.iitk.ac.in/cs657/corpora/hindi/

Bilingual Dictionary - https://github.com/bdrillard/english-hindi-dictionary/blob/master/English-Hindi%20Dictionary.csv

Transliteration Dictionary - https://github.com/anoopkunchukuttan/crowd-indic-transliteration-data/blob/master/crowd_transliterations.hi-en.txt

Parallel Corpora - http://www.cfilt.iitb.ac.in/iitb_parallel/iitb_corpus_download/

