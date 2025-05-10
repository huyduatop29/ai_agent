from langchain_unstructured import UnstructuredLoader
from unstructured.cleaners.core import clean_extra_whitespace
import os 
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
import torch

class Solution:
    def GetData(self, folder_path: str) -> tuple[list[str],list[any]]:
        file_path = [
            os.path.join(folder_path, f)
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]
        for file in file_path:
            loader = UnstructuredLoader(
                file_path,
                post_processors=[clean_extra_whitespace],
                chunking_strategy = "basic",
                max_characters = 500,
                include_orig_elements = False,
            )

        docs = loader.load()

        texts = [doc.page_content for doc in docs]

        model = SentenceTransformer("AITeamVN/Vietnamese_Embedding")
        model_kwargs = {'device' : 'cpu'}
        model.max_seq_length = 2048

        #embeddings = [model.encode(text for text in texts)]

        for i,text in enumerate(texts[0:10]):
            embedding = model.encode(text)
            #print(f'Document {i} : {text}')
            #print(f'embedding {i} : {embedding}')
            #print('\n')
        #print(docs[0:10])
        #print("Number of LangChain documents:", len(docs))
        #print("Length of text in the document:", len(docs[0].page_content))
        return texts, embedding

if __name__ == "__main__":
    folder_path = '/home/quochuy/Development/Rag/Data_test'
    solution = Solution()
    texts, embeddings = solution.GetData(folder_path)

    print(texts[0:10])
    print(embeddings[0:10])



    


    


