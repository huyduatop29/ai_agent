import psycopg2

class PostgresConnect:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="llm_data",
            user="quochuy",
            password="29003"
        )
        self.cur = self.conn.cursor()

    def upload(self, docs: list, embeddings: list):
        for i, doc in enumerate(docs):
            # Insert into documents
            self.cur.execute("""
                INSERT INTO documents (filename, file_directory, source, last_modified, filetype, language)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id;
            """, (
                doc.metadata['filename'],
                doc.metadata['file_directory'],
                doc.metadata['source'],
                doc.metadata['last_modified'],
                doc.metadata['filetype'],
                doc.metadata['languages'][0]
            ))
            document_id = self.cur.fetchone()[0]

            # Insert into chunks
            self.cur.execute("""
                INSERT INTO chunks (document_id, page_number, element_id, page_content)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
            """, (
                document_id,
                doc.metadata.get('page_number'),
                doc.metadata.get('element_id'),
                doc.page_content
            ))
            chunk_id = self.cur.fetchone()[0]

            # Insert into emphasized_text
            for content, tag in zip(
                doc.metadata.get('emphasized_text_contents', []),
                doc.metadata.get('emphasized_text_tags', [])
            ):
                self.cur.execute("""
                    INSERT INTO emphasized_text (chunk_id, content, tag)
                    VALUES (%s, %s, %s);
                """, (chunk_id, content, tag))

            # Insert into embeddings
            self.cur.execute("""
                INSERT INTO embeddings (chunk_id, vector_data)
                VALUES (%s, %s);
            """, (
                chunk_id,
                embeddings[i]
            ))

        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

