import pipeline
import connect



if __name__ == "__main__":
    folder_path = '/home/quochuy/Development/Rag/Datas/'
    solution = pipeline.Solution()
    docs, embeddings, documents = solution.GetData(folder_path)
    con = connect.PostgresConnect()
    con.__init__()
    con.upload(docs,embeddings)

    
