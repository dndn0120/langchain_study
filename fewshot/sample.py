from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import  Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI

import sys
sys.path.append('/Users/jinwook/Documents/langchain/quick_start/')
from langchain_const import *

# 유저 인풋 값
user_input_text = "재료: 닭, 토마토, 우유, 밀가루, 팔각"

# 예제
examples = [
  {
    "input": "재료: 닭고기, 소금, 후추, 마늘",
    "output": "진욱 AI가 알려주는 레시피!!: 닭고기를 작은 조각으로 자릅니다. 소금과 후추로 간을 하고, 팬에 기름을 둘러 마늘을 볶습니다.마늘이 노릇해 지면 닭고기를 넣고 익을 때까지 볶습니다. 완성된 닭고기를 접시에 담아 냅니다."
  },
  {
    "input": "재료: 쌀, 당근",
    "output":"진욱 AI가 알려주는 레시피!!: 쌀을 불려서, 당근이랑 같이 볶아요"
  },
  {
    "input": "재료: 소고기, 토마토, 당근, 소금, 후추, 고추가루",
    "output":"진욱 AI가 알려주는 레시피!!: 소고기를 망치로 두드린다음, 얇게 펴서 후추를 뿌리고, 당근과 토마토를 다져서 고추가루와 함께 볶아요"
  },
  {
    "input": "재료: 레몬, 바닐라, 밀가루",
    "output":"진욱 AI가 알려주는 레시피!!: 밀가루를 반죽해서 빵으로 만든 다음, 레몬과 바닐라를 넣고 오븐에 구우면 완벽"
  },
  {
    "input": "재료: 닭고기, 파, 양파, 대추, 감자, 한약재",
    "output":"진욱 AI가 알려주는 레시피!!: 닭고기를 한번 물에 데친다음, 파, 양파를 반으로 잘라서 준비하고, 대추랑 감자를 넣고 푹 삶아주세요"
  },
]

# 예제 임베딩
example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 선택한 example들 설정
    examples,
    # 유사한 임베딩값을 찾기 위한 임베딩 모델 설정
    OpenAIEmbeddings(openai_api_key=OPENAI_KEY),
    # vector store 설정
    Chroma,
    # 몇개의 가장 유사한 embedding을 찾을 것인지를 설정
    k=2
)

# 예제 연관성 조회
selected_examples = example_selector.select_examples({"input": user_input_text})

# 프롬프트 생성
example_prompt = PromptTemplate(
    input_variables=["input", "output"], 
    template="Input: {input}\nOutput: {output}"
)

# Few Shot 프롬프트 구성
prompt = FewShotPromptTemplate(
    examples=selected_examples, 
    example_prompt=example_prompt,
    suffix="Input : {input}",
    input_variables=["input"],
)

llm = OpenAI(api_key=OPENAI_KEY)

# Output Parser
parser = StrOutputParser()

# Chaining
chain = prompt | llm | parser

print(chain.invoke({"input": user_input_text}))