from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain_const import *

# 올바른 API 키 설정 (환경 변수로 설정하는 것을 권장)

llmOpenAi = OpenAI(api_key=OPENAI_KEY)
llmChatOpenAi = ChatOpenAI(api_key=OPENAI_KEY)

response = llmChatOpenAi.invoke("나는 멋지다")
print(response)