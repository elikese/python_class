# 저번시간 복습

# with
# open -> close 해줘야한다
# with문법을 사용하면 들여쓰기까지 실행되고 알아서 close 된다
with open("./test.txt", "w", encoding="utf-8") as f:
    f.write("Hello World")

# with open(경로, 모드, 인코딩) as 파일 변수(작명):
# 경로는 절대경로(c:aa/bb/cc...), 상대경로("./" : 내가 작성하는 py파일 위치, "../" : 내가 작성하는 py파일 위치의 한단계 상위)
# 모드는 w:write, r:read
# encoding : utf-8(웹표준)

with open("./test.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)

import json

# json : 사실상 python의 dict과 거의 동일한 구조
# 주로 웹 데이터 송수신용으로 쓰인다
with open("./test.json", "w", encoding="utf-8") as f:
    json.dump(["철수", "영희"], f, ensure_ascii=False)

# json.dump(list, map.., file, ensure_ascii -> 아스키변환할건지? 한글은 아스키코드 변환 x)
# python 자료형은 json으로 변환해서 저장해줌

with open("./test.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
# json.load(file) -> file에 있는 data를 python 자료형으로 바꿔서 만들어 줌

from datetime import datetime

# datetime.now() : datetime 자료형으로 현재시간을 나타냄
# datetime.now().strftime("%Y-%m-%d %H:%M") : datetime 자료형을 내가 원하는 포맷의 문자열로 바꿔줌

import os

# 해당경로에 money.json이 없다면
if not os.path.exists("./money.json"):
    with open("./money.json", "w", encoding="utf-8") as f:
        json.dump([], f)


def load_logs():
    with open("./money.json", "r", encoding="utf-8") as f:
        logs = json.load(f)
        return logs


def write_income(log_list):
    money = input("얼마 벌으셨나요 >>> ")

    if not money.isdecimal():
        return

    data = {"금액": int(money), "시간": datetime.now().strftime("%Y-%m-%d %H:%M")}
    log_list.append(data)
    with open("./money.json", "w", encoding="utf-8") as f:
        json.dump(log_list, f, ensure_ascii=False)


def write_expense(log_list):
    money = input("얼마 쓰셨나요 >>> ")

    if not money.isdecimal():
        return

    data = {"금액": -1 * int(money), "시간": datetime.now().strftime("%Y-%m-%d %H:%M")}
    log_list.append(data)
    with open("./money.json", "w", encoding="utf-8") as f:
        json.dump(log_list, f, ensure_ascii=False)


def print_money_log(log_list):
    sum = 0
    print("===== 내역조회 =====")
    for log in log_list:
        print(f"금액: {log['금액']} 거래일시: {log['시간']}")
        sum += log["금액"]
    print(f"합계: {sum}")


while True:
    print("=========== 가계부 ===========")
    print("1. 수입 입력")
    print("2. 지출 입력")
    print("3. 내역 조회")
    print("4. 종료")

    choice = input("선택(1~4) >>>")
    log_list = load_logs()

    if choice == "1":
        write_income(log_list)
    elif choice == "2":
        write_expense(log_list)
    elif choice == "3":
        print_money_log(log_list)
    elif choice == "4":
        print("프로그램을 종료합니다")
        break
    else:
        print("잘못된 입력입니다")
