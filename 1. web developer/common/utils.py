from datetime import datetime

def get_today():
  return datetime.now()

def get_str_today(format='%Y-%m-%d'):
  return get_today().strftime(format)

