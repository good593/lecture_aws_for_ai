import streamlit as st
from groq import Groq
import time

# @st.cache_data # 데이터를 caching 처리 
@st.cache_resource # 객체를 caching 처리 
def get_client():
    return Groq()

def response_from_llm(prompt, message_history=[], model_id:str="llama-3.1-8b-instant"):
    if len(message_history) == 0:
        # 최초 질문
        message_history.append(
            {
                "role": "assistant",
                "content": "You are a helpful assistant. You must answer in Korean.",
            }
        )

    # 사용자 질문 추가
    message_history.append(
        {
            "role": "user",
            "content": prompt,
        },
    )

    streaming = get_client().chat.completions.create(
        model=model_id,
        messages=message_history,
        stream=True
    )

    # return streaming.choices[0].message.content
    for chunk in streaming:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content
            time.sleep(0.05)


