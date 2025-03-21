import streamlit as st
from dotenv import load_dotenv

load_dotenv() # .env 파일을 읽어서 환경변수로 사용할 수 있도록 설정

from common.etl.download import download_of_ticker
from common.etl.constants import TICKER_TYPE
from common.plot import show_plot
from common.sidebar import get_ticker_market
from common.utils import get_today

year = str(get_today().year)
st.title(f"{year}년도 일별 데이터 조회")

selected_ticker_name = get_ticker_market()
selected_ticker = TICKER_TYPE[selected_ticker_name]

st.subheader(f"{selected_ticker.value[2]} 그래프")
df = download_of_ticker(selected_ticker, f"{year}-01-01")
show_plot([(df, selected_ticker.value[2])])

st.subheader(f"{selected_ticker.value[2]} 데이터")
df = df.rename(columns={'Date': '날짜', 'Open': '시가', 'High': '고가', 'Low': '저가', 'Close': '종가', 'Volume': '거래량'})
for col in ['시가', '고가', '저가', '종가', '거래량']:
  df[col] = df[col].map(lambda x: "{:,.0f}".format(x))
st.dataframe(df)
