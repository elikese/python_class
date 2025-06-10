from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# pip install selenium
# pip install webdriver-manager
# pip install openpyxl

# 드라이버 설정 및 네이버 접속
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://naver.com")
# driver.maximize_window()
sleep(1)

# 웹툰 홈으로 이동
webtoon_home_link = driver.find_element(by=By.CSS_SELECTOR, value="#shortcutArea > ul > li:nth-child(9) > a")
webtoon_home_url = webtoon_home_link.get_attribute("href")
driver.get(webtoon_home_url)
sleep(1)
print(f"웹툰 홈: {driver.current_url}")

# 웹툰 메뉴 클릭(실습)
webtoon_link = driver.find_element(by=By.CSS_SELECTOR, value="#menu > li:nth-child(2) > a")
webtoon_link.click()
sleep(1)
print(f"웹툰 페이지: {driver.current_url}")

# 첫 번째 요일(월요일) 탭 클릭
day_tabs = driver.find_elements(by=By.CSS_SELECTOR, value="#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a")
monday_tab = day_tabs[1]  # 월요일 탭
print(f"월요일 탭 클릭: {monday_tab.text}")
monday_tab.click()
sleep(1)

# 첫 번째 웹툰 아이템 찾기
webtoon_items = driver.find_elements(by=By.CSS_SELECTOR, value="#content > div:nth-child(1) > ul > li")  # 전체웹툰리스트
first_webtoon = webtoon_items[0]  # 첫 번째 웹툰만
print(f"첫 웹툰 크롤링 시작")

# 요소까지 스크롤
driver.execute_script("arguments[0].scrollIntoView()", first_webtoon)
sleep(1)

# 이미지 URL 추출
webtoon_img = first_webtoon.find_element(by=By.CSS_SELECTOR, value=".Poster__image--d9XTI")
img_url = webtoon_img.get_attribute("src")

# 제목 추출
webtoon_title = first_webtoon.find_element(by=By.CSS_SELECTOR, value=".ContentTitle__title--e3qXt .text")
title_text = webtoon_title.text

# 작가 추출
webtoon_author = first_webtoon.find_element(by=By.CSS_SELECTOR, value=".ContentAuthor__author--CTAAP")
author_text = webtoon_author.text

# 평점 추출
webtoon_rating = first_webtoon.find_element(by=By.CSS_SELECTOR, value=".Rating__star_area--dFzsb .text")
rating_text = webtoon_rating.text

print(
    f"""
제목: {title_text}
작가: {author_text}
평점: {rating_text}
이미지 URL: {img_url}"""
)

# 드라이버 종료
driver.quit()
