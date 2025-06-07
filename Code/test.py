import psycopg2
import numpy as np
import pipeline
from connect import PostgresConnect
from sentence_transformers import SentenceTransformer
import torch



text = "Trường đại học giao thông vận tải"
sol = pipeline.Solution()
con = PostgresConnect()
text = sol.preprocessing(text)
cur = con.cur



cur.execute("""
        select c.id , c.page_content, e.vector_data 
        from embeddings as e 
        join chunks as c on c.id = e.chunk_id 
        order by c.id asc; 
    """)
rows = cur.fetchall()

model = SentenceTransformer("AITeamVN/Vietnamese_Embedding")
model_kwargs = {'device' : 'cpu'}
model.max_seq_length = 2048
query = model.encode(text)
query = np.array(query)    

similarity = []
for row in rows:
    id = row[0]
    chunk = row[1]
    vector_db = row [2]
    print(type(vector_db))
    '''
    vt = np.array(vector_db, dtype=np.float32)
    score = np.dot(query, vt) / (np.linalg.norm(query) * np.linalg.norm(vt))
    similarity.append((score, vector_db, id, chunk))
    '''
similarity. sort(reverse = True)

#print(similarity[0:5])


