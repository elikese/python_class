import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 가장 많이 쓰는 4가지 방법
print("=== 1. 태그로 찾기 ===")
title = soup.find("title").text
print(title)

print("\n=== 2. 클래스로 찾기 ===")
quotes = soup.find_all("div", class_="quote")
print(f"명언 개수: {len(quotes)}")

print("\n=== 3. CSS 선택자로 찾기 ===")
authors = soup.select(".author")
for author in authors[:3]:
    print(author.text)

print("\n=== 4. 속성으로 찾기 ===")
links = soup.find_all("a", href=True)
print(f"링크 개수: {len(links)}")
