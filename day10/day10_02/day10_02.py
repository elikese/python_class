# JSON 모듈을 임포트하여 파일로부터 데이터를 읽고 쓰는 기능을 제공
import json

# 책 데이터를 저장할 JSON 파일 경로 설정
book_file_path = "./books.json"


# 사용자로부터 책 정보를 입력받아 튜플 형태로 반환하는 함수
def input_book_info():
    title = input("책 제목을 입력하세요 >>")   # 책 제목 입력
    author = input("저자를 입력하세요 >>")     # 저자 입력
    year = input("출판년도를 입력하세요 >>")    # 출판년도 입력
    return (title, author, year)            # 입력값을 튜플로 반환


# JSON 파일로부터 책 목록을 불러오는 함수
def load_books():
    with open(book_file_path, "r", encoding="utf-8") as f:
        return json.load(f)  # 파일 내용을 파싱해서 리스트로 반환


# 책 목록을 JSON 파일로 저장하는 함수
def save_books(book_list):
    with open(book_file_path, "w", encoding="utf-8") as f:
        # 리스트를 JSON 문자열로 변환하여 파일에 저장 (한글깨짐 방지, 보기 좋게 들여쓰기 포함)
        json.dump(book_list, f, ensure_ascii=False, indent=4)


# 입력된 책 정보를 딕셔너리 형태로 구성하여 반환하는 함수
def make_book(title, author, year):
    book = {"title": title, "author": author, "year": year}
    return book


# 메인 실행 루프
while True:
    print("=== 책 관리 시스템 ===")
    print("1. 책 등록")
    print("2. 책 조회")
    print("3. 종료")
    choice = input("선택 >>> ")  # 사용자로부터 메뉴 선택 입력 받기

    if choice == "1":
        # 책 등록
        title, author, year = input_book_info()   # 사용자로부터 책 정보 입력받기
        book = make_book(title, author, year)     # 입력받은 정보를 딕셔너리로 구성
        book_list = load_books()                  # 기존 책 목록 불러오기
        book_list.append(book)                    # 새 책을 목록에 추가
        save_books(book_list)                     # 업데이트된 목록을 파일에 저장

    elif choice == "2":
        # 책 조회
        book_list = load_books()                  # 책 목록 불러오기
        if not book_list:                         # 책 목록이 비어있으면 안내 메시지 출력
            print("등록된 책이 존재하지 않습니다")
            continue
        for book in book_list:
            # 각 책의 정보를 포맷팅하여 출력
            print(
                f"책제목:{book['title']}, 저자:{book['author']}, 출판년도:{book['year']}"
            )

    elif choice == "3":
        # 프로그램 종료
        print("시스템 종료.")
        break

    else:
        # 잘못된 메뉴 번호 입력 시 경고 메시지 출력
        print("잘못된 선택입니다.")
