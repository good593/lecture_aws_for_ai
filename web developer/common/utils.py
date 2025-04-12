import streamlit as st
from datetime import datetime

@st.cache_data
def get_today():
  return datetime.now()

def get_str_today(format='%Y-%m-%d'):
  return get_today().strftime(format)

