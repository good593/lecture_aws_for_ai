import streamlit as st 

from common.db import query

st.title("데이터 베이스 화면")

df = query("show databases;")
st.dataframe(df)
