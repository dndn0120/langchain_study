import sys
sys.path.append('/Users/jinwook/Documents/langchain/quick_start/')
from langchain_const import *
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat = ChatOpenAI(openai_api_key=OPENAI_KEY)   # 기본모델 : gpt-3.5-turbo
# aiMessage = chat.invoke(
#     [
#         HumanMessage(
#             content="이 문장을 영어에서 한국어로 번역하세요 : I love programming."
#         )
#     ]
# )

messages = [
    HumanMessage(
        content="영어를 한국어로 번역하세요."
    ),

    HumanMessage(
        content="i love programming"
    ),
    # AIMessage(content="i love programming"),
    HumanMessage(content="뭐래?"),
]
# aimessage2 = chat.invoke(messages)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "너는 항상 최선의 답을 해줘야해. 근데, 시작할 땐 꼭 '진욱님'이라고 시작해야해",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | chat

demo_ephemeral_chat_history = ChatMessageHistory()

demo_ephemeral_chat_history.add_user_message("내이름은 강진욱이야")


response = chain.invoke({"messages": demo_ephemeral_chat_history.messages})
demo_ephemeral_chat_history.add_ai_message(response)

demo_ephemeral_chat_history.add_user_message("내이름이 뭐라고?")

response = chain.invoke({"messages": demo_ephemeral_chat_history.messages})
demo_ephemeral_chat_history.add_ai_message(response)

demo_ephemeral_chat_history.add_user_message("염소는 닭을 먹어")


response = chain.invoke({"messages": demo_ephemeral_chat_history.messages})
demo_ephemeral_chat_history.add_ai_message(response)

demo_ephemeral_chat_history.add_user_message("오늘 점심 추천 가능?")


response = chain.invoke({"messages": demo_ephemeral_chat_history.messages})
demo_ephemeral_chat_history.add_ai_message(response)

demo_ephemeral_chat_history.add_user_message("염소는 뭘 먹는다고?")


response = chain.invoke({"messages": demo_ephemeral_chat_history.messages})
demo_ephemeral_chat_history.add_ai_message(response)

print(response.content)