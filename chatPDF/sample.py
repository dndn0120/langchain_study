
import sys
sys.path.append('/Users/jinwook/Documents/langchain/quick_start/')
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from chat_pdf_template import *
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough

from langchain_const import *

loader = PyPDFLoader("https://snuac.snu.ac.kr/2015_snuac/wp-content/uploads/2015/07/asiabrief_3-26.pdf")

# PDF 를 로드하고 일정 기준으로 스플릿한다.
pages = loader.load_and_split()

# 스플릿한 데이터를 추가적으로 스플릿한다.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=0)
splits = text_splitter.split_documents(pages)

# 임베딩을 통한 벡터데이터 저장
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=OPENAI_KEY)) # text-embedding-ada-002
retriever = vectorstore.as_retriever()

llmChatOpenAi = ChatOpenAI(model_name=GPT_MODEL, temperature=0, api_key=OPENAI_KEY)

# RunnablePassThrough 공부하기
ragChain = {"ragContext": retriever, "question": RunnablePassthrough()} | ragPromptCustom | llmChatOpenAi

print(ragChain.invoke('한국의 저출산 원인이 뭐야?'))


