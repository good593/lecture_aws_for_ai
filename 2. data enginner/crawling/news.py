import requests
from bs4 import BeautifulSoup
from .constants import NEWS_TYPE


def get_news_from_naver(keyword:NEWS_TYPE):
  # 키워드, URL
  url = f'https://search.naver.com/search.naver?where=news&query={keyword.value[1]}'

  # 웹 페이지 요청
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  # news_tit 부분 필터링
  articles = soup.select('.news_tit')

  # 뉴스 제목
  return [article.text for article in articles]



