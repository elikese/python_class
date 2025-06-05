import requests
from bs4 import BeautifulSoup
import time

# 기본 설정
url = "https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1&divpage=101"

print("뽐뿌 크롤링 시작...")

# 웹페이지 요청
response = requests.get(url)
# 200: 성공, 404:찾을수 없음, 401: 권한부족, 500: 서버에러
print(f"응답 상태코드: {response.status_code}")

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 게시글 목록 찾기
post_rows = soup.find_all("tr", class_="baseList")
print(f"찾은 게시글 수: {len(post_rows)}개")

# 데이터 저장할 리스트
post_list = []

# 각 게시글 정보 추출
for i, row in enumerate(post_rows[:21]):
    print(f"--- {i+1}번째 게시글 처리 중 ---")

    # 썸네일 이미지 추출
    img = row.find("img")
    if img:
        img_url = img.get("src")
        print("이미지: https:" + f"{img_url}")
    else:
        img_url = None
        print("이미지: 없음")

    # 제목, 링크 추출
    title_link = row.find("a", class_="baseList-title")
    if title_link:
        title = title_link.get_text(strip=True)
        link_url = title_link.get("href")
        print(f"제목: {title}")
        print("링크: https://www.ppomppu.co.kr/zboard/" + f"{link_url}")
    else:
        print("제목을 찾을 수 없음")
        continue

    # 작성자 추출
    author_element = row.find("span", class_="baseList-name")
    if author_element:
        author = author_element.get_text(strip=True)
        print(f"작성자: {author}")
    else:
        author = "익명"
        print("작성자: 익명")

    # 시간 추출
    time_element = row.find("time", class_="baseList-time")
    if time_element:
        post_time = time_element.get_text(strip=True)
        print(f"시간: {post_time}")
    else:
        post_time = ""
        print("시간: 정보없음")

    # 데이터 딕셔너리 생성
    post_data = {
        "title": title,
        "author": author,
        "time": post_time,
        "image_url": "https:" + img_url,
        "link_url": "https://www.ppomppu.co.kr/zboard/" + link_url,
    }

    # 리스트에 추가
    post_list.append(post_data)

# 결과 출력
print(f"\n" + "=" * 50)
print(f"크롤링 완료! 총 {len(post_list)}개 게시글 수집")
print("=" * 50)

print(f"\n전체 데이터:")
print(post_list)
