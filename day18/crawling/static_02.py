# 💡 requests는 웹페이지에 접속해서 HTML을 가져오는 라이브러리
# 💡 BeautifulSoup는 가져온 HTML에서 원하는 정보를 쉽게 뽑아낼 수 있도록 도와줌
import requests
from bs4 import BeautifulSoup

# [1단계] 크롤링할 웹사이트 주소 설정
url = "http://quotes.toscrape.com/"

# [2단계] 해당 주소로 요청을 보내고 HTML 내용을 가져옴
response = requests.get(url)

# [3단계] 가져온 HTML을 BeautifulSoup으로 분석하기 (html.parser는 기본 파서)
soup = BeautifulSoup(response.text, "html.parser")

# 💥 가장 많이 쓰는 4가지 찾기 방법 💥
# 방법 1. 태그 이름으로 찾기 (find)
print("=== 1. 태그로 찾기 ===")
# <title> 태그는 페이지 제목을 담고 있음. 보통 브라우저 탭에 표시됨
title_tag = soup.find("title")
title = title_tag.get_text()
# .text는 태그 안의 글자만 추출
print(title)  # 예: Quotes to Scrape

# 방법 2. 클래스 이름으로 찾기 (find_all)
print("\n=== 2. 클래스로 찾기 ===")
# <div class="quote"> 태그들을 모두 가져옴. 각 명언 덩어리 하나씩 포함
quotes = soup.find_all("div", class_="quote")
# 가져온 명언 블록 개수 출력
print(f"명언 개수: {len(quotes)}")  # 예: 10

# 방법 3. CSS 선택자로 찾기 (select)
print("\n=== 3. CSS 선택자로 찾기 ===")
# .author는 <small class="author">처럼 클래스명이 author인 태그를 뜻함
# select()는 CSS 선택자 방식으로 여러 요소를 한꺼번에 찾음
authors = soup.select(".author")  # 리스트 형태로 반환

# 앞에서 찾은 작가 이름 중 처음 3개만 출력
for author in authors[:3]:
    print(author.text)

# 방법 4. 속성으로 찾기 (속성값 조건으로 검색)
print("\n=== 4. 속성으로 찾기 ===")

# <a href="..."> 태그들을 모두 찾기
# href=True는 href 속성이 있는 <a> 태그만 찾겠다는 뜻
links = soup.find_all("a", href=True)
print(links)
# 전체 링크 개수 출력
print(f"링크 개수: {len(links)}")  # 예: 10~20개
