# 중첩 while문
while True:
    print("메뉴: 1.시작 2.종료")
    선택 = input("메뉴(숫자)를 입력하세요 >>")
    if 선택 == "1":
        while True:
            print("메뉴: 1.1번선택 2.2번선택 3.돌아가기")
            선택 = input("메뉴(숫자)를 입력하세요 >>")
            if 선택 == "1":
                print("1번선택")
            elif 선택 == "2":
                print("2번선택")
            elif 선택 == "3":
                print("위메뉴로 돌아갑니다")
                break
    elif 선택 == "2":
        print("시스템 종료")
        break
    else:
        print("숫자를 입력하세요")
        continue

잔액 = 10000  # 초기 잔액 설정
while True:
    print("===== 은행 시스템 메뉴 =====")
    print("1. 시작")
    print("2. 종료")
    선택 = input("메뉴 번호를 입력하세요 >> ")

    if 선택 == "1":
        while True:
            print(f"현재 잔액: {잔액}원")
            print("1. 입금")
            print("2. 출금")
            print("3. 이전 메뉴로 돌아가기")
            선택 = input("메뉴 번호를 입력하세요 >> ")

            if 선택 == "1":
                금액 = int(input("입금할 금액을 입력하세요 >> "))
                잔액 += 금액
                print(f"{금액}원을 입금했습니다.")
            elif 선택 == "2":
                금액 = int(input("출금할 금액을 입력하세요 >> "))
                if 금액 > 잔액:
                    print("잔액이 부족합니다.")
                else:
                    잔액 -= 금액
                    print(f"{금액}원을 출금했습니다.")
            elif 선택 == "3":
                print("메인 메뉴로 돌아갑니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
    elif 선택 == "2":
        print("시스템을 종료합니다. 이용해주셔서 감사합니다")
        break
    else:
        print("숫자만 입력해주세요")
