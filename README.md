The queries is assumed to be given in Hindi and later converted to English

Python files:
---------------------------
cos_sim.py: It takes two files containing feature vectors of all documents and queries. It retrieves 100 docs for each query and saves it in file 'result1.txt'.
doc2feature.py: It takes the embeddings for English words and saves feature vectors for all documents to file 'feature.txt'.
embeddings.py: It takes embeddings of English and Hindi words as well as Hindi-English Dictionary, It saves translated queries in 'expanded-queries.txt'. 
hi_to_eng.py
ir.py
ir_cos_sim.py
merged_embed.py
query2feature.py: It takes embeddings of Hindi words and queries file. It saves the feature vectors of each queries in 'query-feature.txt'. 
transliteration.py 
