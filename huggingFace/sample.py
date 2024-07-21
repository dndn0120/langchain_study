from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain_community.vectorstores import  Chroma

#model_name = "sentence-transformers/all-mpnet-base-v2"
#model_name = "BAAI/bge-large-en-v1.5"  # (2023.11.16 기준 공개모델 중 LeaderBoard 1위 모델)
model_name = "jhgan/ko-sroberta-multitask" # (KorNLU 데이터셋에 학습시킨 한국어 임베딩 모델)
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

sample_texts = [
        "물고기 리스트",
        "고등어",
        "고래",
        "돌고래",
        "범고래",
        "날치",
        "제주산 갈치"
]

documents =  []
for item in range(len(sample_texts)):
    page = Document(page_content=sample_texts[item])
    documents.append(page)

db = Chroma.from_documents(documents, hf)

query = "어류"
docs = db.similarity_search_with_score(query)
print(docs[0])