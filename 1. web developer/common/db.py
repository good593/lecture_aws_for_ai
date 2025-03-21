import os
import streamlit as st

@st.cache_resource(ttl=3600)
def __get_connection(name="mydb", type="sql", dialect="mysql", autocommit=True):
  return st.connection(
    name=name, 
    type=type, 
    autocommit=autocommit, 
    dialect=dialect,
    host=os.getenv("host"),
    username=os.getenv("user_name"),
    password=os.getenv("password"),
    database=os.getenv("database"),
    port=3306
  )

def query(sql, ttl=3600, **kwargs):
  conn = __get_connection()
  return conn.query(sql, ttl=ttl, **kwargs)

