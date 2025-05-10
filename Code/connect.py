import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    post = 5342,
    database = 'rag_document',
    user = 'quochuy'
    password = '29003'
)
cur == conn.cursor()






