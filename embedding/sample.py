import sys
sys.path.append('/Users/jinwook/Documents/langchain/quick_start/')
from langchain_openai import OpenAIEmbeddings
from langchain_const import *
from langchain.docstore.document import Document
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)
from langchain_community.vectorstores import  Chroma

embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
embeddings = embeddings_model.embed_documents([
    "안녕!",
    "빨간색 공",
    "파란색 공",
    "붉은색 공",
    "푸른색 공",
])

sample_texts = [
    "안녕!",
    "빨간색 공",
    "파란색 공",
    "붉은색 공",
    "푸른색 공",
]

sample_spliter_text = "안녕! 빨간색 공 파란색 공 붉은색 공 푸른색 공"

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 5,
    chunk_overlap = 2,
    length_function = len,
    add_start_index = False,
)

documents = []
for item in range(len(sample_texts)):
    page = Document(page_content=sample_texts[item])
    documents.append(page)

document_text_spliter_datas = text_splitter.create_documents([sample_spliter_text])
# print(document_text_spliter_datas)
# print(documents)
db = Chroma.from_documents(documents=documents, embedding=embeddings_model)

query = "레드"
docs = db.similarity_search(query)
print(docs[0].page_content)
