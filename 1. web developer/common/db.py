import os
import streamlit as st

@st.cache_resource(ttl=3600)
def __get_connection(name="mydb", type="sql", dialect="mysql", autocommit=True):
  return st.connection(
    name=name, 
    type=type, 
    autocommit=autocommit, 
    dialect=dialect,
    host=os.getenv("host") if os.getenv("host") is None else "localhost",
    username=os.getenv("username") if os.getenv("username") is None else "root",
    password=os.getenv("password") if os.getenv("password") is None else "root1234",
    database=os.getenv("database") if os.getenv("database") is None else "examplesdb"
  )

def query(sql, ttl=3600, **kwargs):
  conn = __get_connection()
  return conn.query(sql, ttl=ttl, **kwargs)

