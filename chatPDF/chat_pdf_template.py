from langchain.prompts import PromptTemplate

chatTemplate = """
다음은 채팅 기록을 담고 있는 CSV 파일의 내용입니다. CSV 파일은 세 개의 열로 구성되어 있습니다:
- `Date`: 채팅 메시지가 전송된 시간
- `User`: 메시지를 보낸 사용자
- `Message`: 사용자가 보낸 채팅 메시지

CSV 파일의 데이터는 아래와 같은 형식으로 제공됩니다:

{ragContext}

이제 주어진 CSV 데이터를 사용하여, 채팅 기록을 분석하거나 요약해 주세요.
"""
ragPromptCustom = PromptTemplate.from_template(chatTemplate)
