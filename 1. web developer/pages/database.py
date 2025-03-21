import streamlit as st 

from common.db import query

st.title("데이터 베이스 화면")

prompt = st.text_input(label="SQL 입력", value="show databases;")

if st.button("실행"):
    df = query(prompt)
    st.dataframe(df)
