import json
from datetime import datetime

# 할 일 목록을 저장하는 파일 경로
todo_file_path = "./todo.json"


# 파일에서 todo 리스트를 불러오는 함수
def load_todo():
    with open(todo_file_path, "r", encoding="utf-8") as f:
        todo_list = json.load(f)  # JSON 파일을 파싱하여 파이썬 리스트로 반환
    return todo_list


# 새로운 할 일을 생성하는 함수
def make_todo():
    todo_title = input("할일입력>> ")  # 사용자로부터 할 일 제목 입력 받기
    is_finish = False  # 기본값은 미완료 상태
    create_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분")  # 현재 시간 저장

    # 할 일을 하나의 딕셔너리로 구성
    todo = {
        "title": todo_title,
        "is_finish": is_finish,
        "create_time": create_time,
    }
    return todo


# 새 할 일을 리스트에 추가하고 JSON 파일에 저장하는 함수
def add_todo(todo, todo_list):
    todo_list.append(todo)  # 리스트에 추가
    with open(todo_file_path, "w", encoding="utf-8") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent=4)  # 파일에 저장

    print(f"{todo['title']}가 성공적으로 추가되었습니다")  # 사용자에게 알림


# 현재 리스트를 파일에 저장하는 함수 (수정/삭제 시 호출)
def save_todo(todo_list):
    with open(todo_file_path, "w", encoding="utf-8") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent=4)


# 완료되지 않은 할 일만 출력하는 함수
def print_not_finish_list(todo_list):
    not_finish_list = list(filter(lambda todo: not todo["is_finish"], todo_list))  # 필터링

    if not not_finish_list:
        print("현재 미완료 된 할일이 없습니다")
        return

    print("======================================================================")
    for index, todo in enumerate(not_finish_list):  # 인덱스와 함께 출력
        print(
            f"번호:{index}, 할일:{todo['title']}, 완료:{todo['is_finish']}, 만든시간:{todo['create_time']}"
        )
    print("======================================================================")


# 사용자 입력이 유효한 인덱스인지 검사하는 함수
def is_valid_index(todo_index, todo_list):
    if not todo_index.isdecimal():  # 숫자가 아닌 입력이면 False
        print("숫자를 입력하세요")
        return False

    todo_index = int(todo_index)
    if not 0 <= todo_index < len(todo_list):  # 범위 검사
        print("올바른 번호를 입력하세요")
        return False

    return True


# 특정 인덱스의 할 일을 완료 상태로 표시
def finish_todo(todo_index, todo_list):
    todo_index = int(todo_index)
    todo_list[todo_index]["is_finish"] = True
    return todo_list


# 특정 인덱스의 할 일을 삭제
def delete_todo(todo_index, todo_list):
    todo_index = int(todo_index)
    todo_list.pop(todo_index)
    return todo_list


# 프로그램 실행 루프
while True:
    # 메뉴 출력
    print("====== 메뉴 ======")
    print("1. 할일 추가")
    print("2. 할일 확인")
    print("3. 할일 완료")
    print("4. 할일 삭제")

    choice = input("메뉴 선택(1~4) >>> ")  # 사용자 선택 입력

    if choice == "1":
        # 할 일 추가
        todo = make_todo()  # 새 할 일 생성
        todo_list = load_todo()  # 기존 목록 불러오기
        add_todo(todo, todo_list)  # 추가 및 저장
    elif choice == "2":
        # 할 일 확인
        todo_list = load_todo()
        print_not_finish_list(todo_list)
    elif choice == "3":
        # 할 일 완료 처리
        todo_list = load_todo()
        print_not_finish_list(todo_list)  # 미완료 목록 출력
        index_number = input("완료할 할일의 번호를 입력하세요 >> ")
        if is_valid_index(index_number, todo_list):
            finish_todo_list = finish_todo(index_number, todo_list)  # 완료 표시
            save_todo(finish_todo_list)
    elif choice == "4":
        # 할 일 삭제 처리
        todo_list = load_todo()
        print_not_finish_list(todo_list)  # 미완료 목록 출력
        index_number = input("삭제할 할일의 번호를 입력하세요 >> ")
        if is_valid_index(index_number, todo_list):
            deleted_todo_list = delete_todo(index_number, todo_list)  # 삭제
            save_todo(deleted_todo_list)
    else:
        print("잘못된 입력입니다")  # 1~4 외의 숫자 처리
