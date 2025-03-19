import streamlit as st

@st.cache_resource(ttl=3600)
def __get_connection(name="mydb", type="sql", autocommit=True):
  return st.connection(name=name, type=type, autocommit=autocommit)

def query(sql, ttl=3600, **kwargs):
  conn = __get_connection()
  return conn.query(sql, ttl=ttl, **kwargs)

