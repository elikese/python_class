# 📦 requests와 BeautifulSoup 라이브러리를 불러옵니다.
# requests: 웹사이트에 접속해서 HTML 데이터를 가져올 수 있게 해주는 도구
# BeautifulSoup: 가져온 HTML 데이터를 정리해주는 라이브러리(파서)
import requests
from bs4 import BeautifulSoup

# [1단계] 크롤링할 웹페이지의 주소(URL)를 변수에 저장합니다.
url = "http://quotes.toscrape.com/"

# requests.get() 함수로 해당 웹페이지의 HTML 내용을 요청합니다.
# 이 함수는 웹페이지 전체 소스를 가져옵니다.
response = requests.get(url)

# [2단계] 가져온 HTML 내용을 BeautifulSoup을 이용해 파싱(구조화)합니다.
# "html.parser"는 HTML 문서를 해석하는 파서(parser)를 지정한 것입니다.
soup = BeautifulSoup(response.text, "html.parser")


# [3단계] 웹페이지에서 우리가 원하는 데이터(명언과 작가)를 찾아냅니다.
# HTML 코드 중에서 <div class="quote">인 모든 요소를 가져옵니다.
# 이 요소들 안에 명언과 작가 정보가 들어있습니다.
quotes = soup.find_all("div", class_="quote")

# quotes 리스트 안에는 명언이 여러 개 들어있습니다.
# 하나씩 꺼내면서 명언의 텍스트와 작가를 출력합니다.
for quote in quotes:
    # <span class="text"> 안에 있는 실제 명언 텍스트를 가져옵니다.
    text = quote.find("span", class_="text").text

    # <small class="author"> 안에 있는 작가 이름을 가져옵니다.
    author = quote.find("small", class_="author").text

    # 명언과 작가를 보기 좋게 출력합니다.
    print(f'"{text}" - {author}')

# 크롤링이 끝났다는 메시지를 출력합니다.
print("🎉 첫 크롤링 성공!")
