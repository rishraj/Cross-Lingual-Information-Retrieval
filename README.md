The queries is assumed to be given in Hindi and later converted to English

Python files:
---------------------------
cos_sim.py: It takes two files containing feature vectors of all documents and queries. It retrieves 100 docs for each query and saves it in file 'result1.txt'.
doc2feature.py: It takes the embeddings for English words and saves feature vectors for all documents to file 'feature.txt'.
embeddings.py: It takes embeddings of English and Hindi words as well as Hindi-English Dictionary, It saves translated queries in 'expanded-queries.txt'. 

hi_to_eng.py : It is for the transliteration part. It takes Hindi word and script of the word (i.e. Devanagiri(devanagiri)) and script of the output word (i.e Roman(roman), Harvard-kyoto(hk)) and generate transliterate word.

ir.py

ir_cos_sim.py : It takes Hindi query file, Bilingual dictionary, transliteration dictionary, word2vec word embeddings and generate a English query file(english_queries.txt). It is for the dictinary based approach with cosine similarity to remove the ambiguity.

merged_embed.py : It takes two file one is parallel corpus for Hindi and the other is parallel corpus for English. And generate merged word embeddings, that is by merging two sentence (one from Hindi and the other from English) and then using gensim to generate word2vec for words.

query2feature.py: It takes embeddings of Hindi words and queries file. It saves the feature vectors of each queries in 'query-feature.txt'. 
