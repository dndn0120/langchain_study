from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from template import *
from langchain_const import *

# 올바른 API 키 설정 (환경 변수로 설정하는 것을 권장)

llmChatOpenAi = ChatOpenAI(api_key=OPENAI_KEY)

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("user", humanInput)
])

chain = prompt | llmChatOpenAi
print(chain.invoke({"input: 회사생활"}))