# todo-list 만들기

import json


# 메뉴선택 숫자 검증 함수
def menu_choice_validator(num):
    if not num.isdecimal():
        return {"message": "숫자를 입력하세요", "valid": False}

    int_num = int(num)
    if int_num > 4 or int_num < 1:
        return {"message": "1~4 사이를 입력하세요", "valid": False}

    return {"message": "유효한 접근입니다", "valid": True}


while True:
    print("====== 메뉴 ======")
    print("1. 일정추가")
    print("2. 일정확인")
    print("3. 일정수정")
    print("4. 일정삭제")
    choice = input("메뉴 선택(1~4) >>> ")
    result = menu_choice_validator(choice)
    if not result["valid"]:
        print(result["message"])
        continue
    else:
        print(result["message"])

    if choice == "1":
        pass # 일정을 만들어서 추가하는 코드
    if choice == "2":
        pass #
    if choice == "3":
        pass
    if choice == "4":
        pass
