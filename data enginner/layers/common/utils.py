from datetime import datetime, timedelta

def get_today():
  return datetime.now()

def get_str_today(format='%Y-%m-%d'):
  return get_today().strftime(format)

def get_str_before_endday(enddate, before_days=7, format='%Y-%m-%d'):
  datetime_enddate = datetime.strptime(enddate, format)
  return (datetime_enddate - timedelta(days=before_days)).strftime(format)
