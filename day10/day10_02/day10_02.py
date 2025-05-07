# JSON을 통해서 파일을 저장하고, 불러오기
import json

book_file_path = "./books.json"


# input데이터를 리턴해주는 함수
def input_book_info():
    title = input("책 제목: ")
    author = input("저자: ")
    year = input("출판년도: ")
    return (title, author, year)


# JSON에 있는 data를 불러오는 함수
def load_books():
    with open(book_file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# book_list를 받아서, JSON으로 변환해서 저장하는 함수
def save_books(book_list):
    with open(book_file_path, "w", encoding="utf-8") as f:
        json.dump(book_list, f, ensure_ascii=False, indent=4)


# input으로 받은 데이터를 dict로 묶고 리턴하는 함수
def make_book(title, author, year):
    book = {"제목": title, "저자": author, "출판년도": year}
    return book


while True:
    print("=== 책 관리 시스템 ===")
    print("1. 책 등록")
    print("2. 책 조회")
    print("3. 종료")
    choice = input("선택 >>> ")

    if choice == "1":
        title, author, year = input_book_info()
        # input data를 기반으로 책을 등록하는 코드
        book = make_book(title, author, year)
        book_list = load_books()
        book_list.append(book)
        save_books(book_list)
    elif choice == "2":
        # 책을 조회하는 코드
        book_list = load_books()
        if not book_list:
            print("등록된 책이 존재하지 않습니다")
            continue
        for book in book_list:
            print(
                f"책제목:{book['제목']}, 저자:{book['저자']}, 출판년도:{book['출판년도']}"
            )
    elif choice == "3":
        print("시스템 종료.")
        break
    else:
        print("잘못된 선택입니다.")
