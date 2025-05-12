from langchain_unstructured import UnstructuredLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from unstructured.cleaners.core import clean_extra_whitespace
from sentence_transformers import SentenceTransformer
import torch
import os

from collections import Counter, defaultdict
import string

class Solution:

    def clean_word(self, w: str) -> str:
        letters = set('aáàảãạăaáàảãạăắằẳẵặâấầẩẫậbcdđeéèẻẽẹêếềểễệfghiíìỉĩịjklmnoóòỏõọôốồổỗộơớờởỡợpqrstuúùủũụưứừửữựvwxyýỳỷỹỵz0123456789')
        new_w = ''
        for letter in w:
            if letter.lower() in letters or letter == '.':
                new_w += letter.lower()
        return new_w
    
    def preprocessing(self, doc:str) -> str:
        doc = doc.replace('\n', ' ').replace('==', ' ')
        words = doc.split()
        cleaned_words = [self.clean_word(word) for word in words]
        new_doc = ' '.join(cleaned_words)
        return new_doc
    

    def GetData(self, folder_path: str) -> tuple[list[str], list[any], list[str]]:
        file_path = [
            os.path.join(folder_path, f)
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]
        for file in file_path:
            loader_doc = UnstructuredLoader(file_path)
            loader_chunk = UnstructuredLoader(
                file_path,
                post_processors=[clean_extra_whitespace],
                chunking_strategy = "basic",
                max_characters = 500,
                include_orig_elements = False,
            )

        docs = loader_chunk.load()
        documents = loader_doc.load()
        
        model = SentenceTransformer("AITeamVN/Vietnamese_Embedding")
        model_kwargs = {'device' : 'cpu'}
        model.max_seq_length = 2048

        embedding_store = []
        for doc in docs:
            doc.page_content = self.preprocessing(doc.page_content)
            embedding = model.encode(doc.page_content)
            embedding_store.append(embedding)

        for text in documents:
            text.page_content = self.preprocessing(text.page_content)

        return docs, embedding_store, documents  

if __name__ == "__main__":
    folder_path = '/home/quochuy/Development/Rag/Data_test'
    solution = Solution()
    texts, embeddings, documents = solution.GetData(folder_path)

    print(texts[0:10])
    print(embeddings[0:10])
    print(documents[0:10])


    


    


    


