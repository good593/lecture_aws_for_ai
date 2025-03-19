import streamlit as st

from .search.constants import TICKER_TYPE

def get_ticker_market():
  selected_ticker_name = st.sidebar.selectbox("선택해주세요."
                                              , TICKER_TYPE.__members__.keys()
                                              , format_func=lambda x: TICKER_TYPE[x].value[2])
  return selected_ticker_name


