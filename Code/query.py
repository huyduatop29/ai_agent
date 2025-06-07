import psycopg2
import numpy as np
import pipeline
from connect import PostgresConnect
from sentence_transformers import SentenceTransformer
import torch
import ast

def psql_query(cur, text_query : str) -> list:
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
    query = model.encode(text_query)
    query = np.array(query)    

    similarity = []
    for row in rows:
        id = row[0]
        chunk = row[1]
        vector_db = row [2]     
        vt = np.array(ast.literal_eval(vector_db), dtype=np.float32)
        score = np.dot(query, vt) / (np.linalg.norm(query) * np.linalg.norm(vt))

        similarity.append((score, id, chunk))

    similarity. sort(reverse = True)

    return similarity[0:5]

            
if __name__ == "__main__":
    text = "thế nào là học máy"
    sol = pipeline.Solution()
    con = PostgresConnect()
    text = sol.preprocessing(text)
    cur = con.cur
    top_k = psql_query(cur, text)
    print(top_k)
    con.close()
