# requests: 웹사이트에 접속해서 HTML 데이터를 가져올 수 있게 해주는 도구
# BeautifulSoup: 가져온 HTML 데이터를 정리해주는 라이브러리(파서)
import requests
from bs4 import BeautifulSoup

# 크롤링할 웹페이지의 주소(URL)를 변수에 저장합니다.
url = "http://quotes.toscrape.com/"

# requests.get() 함수로 해당 웹페이지의 HTML 내용을 요청합니다.
# 이 함수는 웹페이지 전체 소스를 가져옵니다.
response = requests.get(url)
# 가져온 HTML 내용을 BeautifulSoup을 이용해 파싱(구조화)합니다.
# "html.parser"는 HTML 문서를 해석하는 파서(parser)를 지정한 것입니다.
soup = BeautifulSoup(response.text, "html.parser")

# 1. find() 연습 - 첫 번째 요소만 가져오기
# 페이지 제목 가져오기
title = soup.find("title")
print(f"페이지 제목: {title.get_text()}")

# 첫 번째 명언 div 가져오기
first_quote = soup.find("div", class_="quote")
quote_text = first_quote.find("span", class_="text").get_text()
quote_author = first_quote.find("small", class_="author").text
print(f"\n첫 번째 명언:")
print(f"내용: {quote_text}")
print(f"작가: {quote_author}")

# 첫 번째 태그만 가져오기
first_tag = first_quote.find("a", class_="tag")
print(f"첫 번째 태그: {first_tag.text}")

print("=" * 60)

# 2. find_all() 연습 - 모든 요소 가져오기
# 모든 명언 div 가져오기
all_quotes = soup.find_all("div", class_="quote")
print(f"총 명언 개수: {len(all_quotes)}")

print("\n모든 명언 목록:")
for i, quote in enumerate(all_quotes):
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    print(f"{i + 1}. {author}: {text[:50]}...")

print("\n" + "=" * 60)

# 3. select() 연습 - CSS 선택자 사용
print("\n3. select() 연습")
print("-" * 30)

# CSS 선택자로 명언 가져오기
quotes_by_css = soup.select(".quote")  # 항상 list반환
print(f"CSS 선택자로 찾은 명언 개수: {len(quotes_by_css)}")
for i, quote in enumerate(quotes_by_css):
    text = quote.select(".text")[0].get_text()
    author = quote.select(".author")[0].get_text()
    print(f"{i + 1}. {author}: {text[:50]}...")

# 복합 선택자로 명언 텍스트만 가져오기
quote_texts = soup.select(".quote .text")
print(quote_texts)
print(f"명언 텍스트 갯수 : ({len(quote_texts)}개)")
for i, text in enumerate(quote_texts[:3]):  # 처음 3개만
    print(f"{i + 1}. {text.text[:60]}...")

# 작가 정보 가져오기
authors_by_css = soup.select(".quote .author")
print(f"작가 정보 갯수 : ({len(authors_by_css)}개)")
for author in authors_by_css[:3]:  # 처음 3개만
    print(f"- {author.get_text()}")

# Top Ten tags 가져오기
top_tags = soup.select(".tags-box .tag")  # .tags-box .tag-item .tag 안해도 됨. 깊이탐색이니까
print(f"Top Ten 태그들")
for i, tag in enumerate(top_tags):
    print(f"{i+1}위 : {tag.get_text()}")

print("=" * 60)

# 4. 고급 활용 - 특정 조건으로 찾기
print("\n4. 고급 활용")
print("-" * 30)

# 'inspirational' 태그가 있는 명언 찾기
inspirational_quotes = []
for quote in all_quotes:
    tags = quote.find_all("a", class_="tag")
    tag_texts = [tag.text for tag in tags]
    if "inspirational" in tag_texts:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        inspirational_quotes.append((author, text))

print(f"\n'inspirational' 태그가 있는 명언 ({len(inspirational_quotes)}개):")
for author, text in inspirational_quotes:
    print(f"- {author}: {text[:50]}...")

# Albert Einstein의 명언만 찾기(실습)
einstein_quotes = []
for quote in all_quotes:
    author = quote.find("small", class_="author").get_text()
    if author == "Albert Einstein":
        text = quote.find("span", class_="text").get_text()
        einstein_quotes.append(text)

print(f"Albert Einstein의 명언 ({len(einstein_quotes)}개):")
for i, quote in enumerate(einstein_quotes, 1):
    print(f"{i}. {quote}")


print("\n" + "=" * 60)


######################################################################################################


# 5. 실전 데이터 추출
print("\n5. 실전 데이터 추출")
print("-" * 30)


def extract_all_quotes(soup):
    """모든 명언 정보를 딕셔너리 형태로 추출"""
    quotes_data = []

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        # 텍스트 추출
        text = quote.find("span", class_="text").get_text().strip()

        # 작가 추출
        author = quote.find("small", class_="author").get_text()

        # 작가 정보 페이지 링크 추출
        author_link = quote.find("a").get("href") if quote.find("a") else None

        # 태그들 추출
        tags = []
        for tag in quote.find_all("a", class_="tag"):
            tags.append(tag.get_text())

        # tags = [tag.text for tag in quote.find_all("a", class_="tag")]

        quote_data = {"text": text, "author": author, "author_link": author_link, "tags": ", ".join(tags), "tag_count": len(tags)}
        quotes_data.append(quote_data)

    return quotes_data


# 모든 명언 데이터 추출
quotes_data = extract_all_quotes(soup)

print("추출된 명언 데이터 샘플:")
for i, quote in enumerate(quotes_data[:2], 1):
    print(f"\n{i}번째 명언:")
    print(f"텍스트: {quote.get('text')[:60]}...")
    print(f"작가: {quote.get('author')}")
    print(f"링크: {quote.get('author_link')}")
    print(f"태그: {quote.get('tags')}")
    print(f"태그 개수: {quote.get('tag_count')}")

print("=" * 60)

# 6. select_one() vs find() 비교
print("\n6. select_one() vs find() 비교")
print("-" * 30)

# find() 방식
title_find = soup.find("title").text
first_quote_find = soup.find("div", class_="quote")
first_author_find = first_quote_find.find("small", class_="author").text

# select_one() 방식
title_select = soup.select_one("title").text
first_quote_select = soup.select_one(".quote")
first_author_select = first_quote_select.select_one(".author").text

print(f"find() 결과 - 제목: {title_find}")
print(f"select_one() 결과 - 제목: {title_select}")

print(f"find() 결과 - 첫 번째 작가: {first_author_find}")
print(f"select_one() 결과 - 첫 번째 작가: {first_author_select}")
