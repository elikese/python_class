import requests
from bs4 import BeautifulSoup
import time


def crawl_ppomppu_page(page_num):
    # 기본 설정
    url = f"https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page={page_num}&divpage=101"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    print(f"뽐뿌 {page_num}페이지 크롤링 시작...")

    # 웹페이지 요청
    response = requests.get(url, headers=headers)
    print(f"응답 상태코드: {response.status_code}")

    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 게시글 목록 찾기
    post_rows = soup.find_all("tr", class_="baseList")
    print(f"찾은 게시글 수: {len(post_rows)}개")

    # 데이터 저장할 리스트
    post_list = []

    # 각 게시글 정보 추출
    for i, row in enumerate(post_rows):
        print(f"\n--- {i+1}번째 게시글 처리 중 ---")

        # 제목 추출
        title_link = row.find("a", class_="baseList-title")
        if title_link:
            title = title_link.get_text(strip=True)
            print(f"제목: {title}")
        else:
            print("제목을 찾을 수 없음")
            continue

        # 쇼핑몰 정보 추출
        preface = row.find("em", class_="subject_preface")
        if preface:
            shop = preface.get_text(strip=True)
            print(f"쇼핑몰: {shop}")
        else:
            shop = "기타"
            print("쇼핑몰: 기타")

        # 작성자 추출
        author_elem = row.find("span", class_="baseList-name")
        if author_elem:
            author = author_elem.get_text(strip=True)
            print(f"작성자: {author}")
        else:
            author = "익명"
            print("작성자: 익명")

        # 시간 추출
        time_elem = row.find("time", class_="baseList-time")
        if time_elem:
            post_time = time_elem.get_text(strip=True)
            print(f"시간: {post_time}")
        else:
            post_time = ""
            print("시간: 정보없음")

        # 조회수 추출
        views_elem = row.find("td", class_="baseList-views")
        if views_elem:
            views = views_elem.get_text(strip=True)
            print(f"조회수: {views}")
        else:
            views = "0"
            print("조회수: 0")

        # 썸네일 이미지 추출
        img_elem = row.find("img")
        if img_elem:
            img_url = img_elem.get("src")
            print(f"이미지: {img_url}")
        else:
            img_url = None
            print("이미지: 없음")

        # 데이터 딕셔너리 생성
        post_data = {"title": title, "shop": shop, "author": author, "time": post_time, "views": views, "image_url": img_url}

        # 리스트에 추가
        post_list.append(post_data)

    # 결과 출력
    print(f"\n" + "=" * 50)
    print(f"{page_num}페이지 크롤링 완료! 총 {len(post_list)}개 게시글 수집")
    print("=" * 50)

    return post_list


# 전체 데이터 저장할 리스트
all_data = []
total_page_num = 5

# 3페이지 크롤링
for page in range(1, total_page_num + 1):
    page_data = crawl_ppomppu_page(page)
    all_data.extend(page_data)

    print(f"\n{page}페이지 데이터 추가됨. 현재 총 {len(all_data)}개")

    # 다음 페이지 전에 잠시 대기
    if page < 3:
        time.sleep(2)

print(f"\n최종 결과:")
print(f"총 {len(all_data)}개의 게시글 수집 완료!")

print(f"\n전체 데이터:")
print(all_data)
