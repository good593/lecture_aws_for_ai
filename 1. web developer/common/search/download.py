import yfinance as yf
import pandas as pd

from .constants import TICKER_TYPE
from common.exception import SearchError
from common.utils import get_str_today

def download_of_ticker(ticker_type: TICKER_TYPE, startdate: str, enddate: str=None) -> pd.DataFrame:
  if not isinstance(ticker_type, TICKER_TYPE):
    raise SearchError('올바른 ticker_type이 아닙니다.') 
  
  ticker = ticker_type.value[1]
  if not enddate:
    enddate = get_str_today()
  
  df = yf.download(ticker, startdate, enddate, auto_adjust=True)
  df = df.droplevel('Ticker', axis=1)
  df.reset_index(inplace=True)
  df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
  return df

