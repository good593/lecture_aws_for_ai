import os 
import boto3
import streamlit as st
from dotenv import load_dotenv

@st.cache_data # 데이터를 caching 처리 
def __set_api_key():
  GROQ_API_KEY = os.environ.get('GROQ_API_KEY', None)
  
  if not GROQ_API_KEY:
    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(Name='/TEST/CICD/STREAMLIT/GROQ_API_KEY', WithDecryption=True)
    os.environ['GROQ_API_KEY'] = parameter['Parameter']['Value']


def init_chatbot():
  load_dotenv()
  __set_api_key()

  if "messages" not in st.session_state:
    st.session_state.messages = []



