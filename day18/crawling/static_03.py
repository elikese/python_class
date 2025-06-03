import requests
from bs4 import BeautifulSoup
import time


def crawl_multiple_pages(num):
    all_data = []

    for page in range(1, num + 1):  # 1~3페이지
        url = f"http://quotes.toscrape.com/page/{page}/"
        print(f"크롤링 중: 페이지 {page}")

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            data = {"text": quote.find("span", class_="text").text, "author": quote.find("small", class_="author").text, "page": page}
            all_data.append(data)

        time.sleep(0.5)  # 서버 부하 방지

    return all_data


data_list = crawl_multiple_pages(3)
print(data_list)
print(f"총 {len(data_list)}개 데이터 수집 완료!")
