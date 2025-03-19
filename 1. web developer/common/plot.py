import streamlit as st 
import pandas as pd
import plotly.graph_objects as go

def show_plot(lst_data: list[tuple[pd.DataFrame, str]]):
  # Figure 생성
  fig = go.Figure()
  for df, name in lst_data:
    fig.add_trace(go.Candlestick(x=df['Date'],open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'], name=name))

  fig.update_layout(xaxis_rangeslider_visible=False)
  st.plotly_chart(fig)



