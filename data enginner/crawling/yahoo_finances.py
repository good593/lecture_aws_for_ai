import yfinance as yf
import pandas as pd
from .constants import TICKER_TYPE
from layers.common.utils import get_str_today, get_str_before_endday


def download_of_ticker(ticker_type: TICKER_TYPE, enddate: str=None) -> pd.DataFrame:
  if not isinstance(ticker_type, TICKER_TYPE):
    raise SearchError('올바른 ticker_type이 아닙니다.') 
  
  ticker = ticker_type.value[1]
  if not enddate:
    enddate = get_str_today()

  startdate = get_str_before_endday(enddate)
  return yf.download(ticker, startdate, enddate, auto_adjust=True)


