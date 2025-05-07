# todo-list 만들기

import json
from datetime import datetime

todo_file_path = "./todo.json"


def load_todo():
    with open(todo_file_path, "r", encoding="utf-8") as f:
        todo_list = json.load(f)
    return todo_list


# todo라는 dict를 만들어 주는 함수
def make_todo():
    todo_title = input("할일입력>> ")
    is_finish = False
    create_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분")
    todo = {
        "title": todo_title,
        "is_finish": is_finish,
        "create_time": create_time,
    }
    return todo


def add_todo(todo, todo_list):
    todo_list.append(todo)
    with open(todo_file_path, "w", encoding="utf-8") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent=4)

    print(f"{todo['title']}가 성공적으로 추가되었습니다")


def save_todo(todo_list):
    with open(todo_file_path, "w", encoding="utf-8") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent=4)


def print_not_finish_list(todo_list):
    not_finish_list = list(filter(lambda todo: not todo["is_finish"], todo_list))

    if not not_finish_list:
        print("현재 미완료 된 할일이 없습니다")
        return

    print("======================================================================")
    for index, todo in enumerate(not_finish_list):
        print(
            f"번호:{index}, 할일:{todo['title']}, 완료:{todo['is_finish']}, 만든시간:{todo['create_time']}"
        )
    print("======================================================================")


def is_valid_index(todo_index, todo_list):
    if not todo_index.isdecimal():
        print("숫자를 입력하세요")
        return False

    todo_index = int(todo_index)
    if not 0 <= todo_index < len(todo_list):
        print("올바른 번호를 입력하세요")
        return False

    return True


def finish_todo(todo_index, todo_list):
    todo_index = int(todo_index)
    todo_list[todo_index]["is_finish"] = True
    return todo_list


def delete_todo(todo_index, todo_list):
    todo_index = int(todo_index)
    todo_list.pop(todo_index)
    return todo_list


while True:
    print("====== 메뉴 ======")
    print("1. 할일 추가")
    print("2. 할일 확인")
    print("3. 할일 완료")
    print("4. 할일 삭제")
    choice = input("메뉴 선택(1~4) >>> ")

    if choice == "1":
        todo = make_todo()
        todo_list = load_todo()
        add_todo(todo, todo_list)
        pass  # 일정을 만들어서 추가하는 코드
    elif choice == "2":
        todo_list = load_todo()
        print_not_finish_list(todo_list)
        pass
    elif choice == "3":
        todo_list = load_todo()
        print_not_finish_list(todo_list)
        index_number = input("완료할 할일의 번호를 입력하세요 >> ")
        if is_valid_index(index_number, todo_list):
            finish_todo_list = finish_todo(index_number, todo_list)
            save_todo(finish_todo_list)
    elif choice == "4":
        todo_list = load_todo()
        print_not_finish_list(todo_list)
        index_number = input("삭제할 할일의 번호를 입력하세요 >> ")
        if is_valid_index(index_number, todo_list):
            deleted_todo_list = delete_todo(index_number, todo_list)
            save_todo(deleted_todo_list)
    else:
        print("잘못된 입력입니다")
