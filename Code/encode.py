from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
import torch

model = SentenceTransformer("AITeamVN/Vietnamese_Embedding")
model_kwargs = {'device' : 'cpu'}
model.max_seq_length = 2048
sentences_1 = ["Trí tuệ nhân tạo là gì", "Lợi ích của giấc ngủ"]
sentences_2 = ["Trí tuệ nhân tạo là công nghệ giúp máy móc suy nghĩ và học hỏi như con người. Nó hoạt động bằng cách thu thập dữ liệu, nhận diện mẫu và đưa ra quyết định.", 
               "Giấc ngủ giúp cơ thể và não bộ nghỉ ngơi, hồi phục năng lượng và cải thiện trí nhớ. Ngủ đủ giấc giúp tinh thần tỉnh táo và làm việc hiệu quả hơn."]
query_embedding = model.encode(sentences_1)
doc_embeddings = model.encode(sentences_2)
similarity = query_embedding @ doc_embeddings.T
print(similarity)


