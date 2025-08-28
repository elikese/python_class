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

# 도서 관리 시스템
책창고 = []
while True:
    print("===== 도서 관리 시스템 메뉴 =====")
    print("1. 시작")
    print("2. 종료")
    선택 = input("메뉴 번호를 입력하세요 >> ")
    if 선택 == "1":
        while True:
            print("1. 도서 등록")
            print("2. 도서 검색")
            print("3. 도서 대출")
            print("4. 이전 메뉴로 돌아가기")
            선택 = input("메뉴 번호를 입력하세요 >> ")
            if 선택 == "1":
                책 = input("등록할 도셔명을 입력해 주세요 >> ")
                책창고.append(책)
                print(f"{책}이을 등록되었습니다.")
            elif 선택 == "2":
                도서명 = input("검색하실 도서명을 입력해 주세요 >> ")
                if 도서명 == "":
                    print(책창고)
                else:
                    검색결과 = []
                    for 책 in 책창고:
                        if 책.startswith(도서명):
                            검색결과.append(책)
                    print(검색결과)
            elif 선택 == "3":
                print(f"현재 현황:{책창고}")
                대출책 = input("대출하실 도서명을 입력해 주세요 >> ")
                책존재여부 = False
                for 책 in 책창고:
                    if 책 == 대출책:
                        print(f"{책}이 대출되었습니다!")
                        책존재여부 = True
                        책창고.remove(대출책)
                        break
                if not 책존재여부:
                    print("해당 책은 존재하지 않습니다.")
            elif 선택 == "4":
                print("메인 메뉴로 돌아갑니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
    elif 선택 == "2":
        print("시스템을 종료합니다. 이용해주셔서 감사합니다")
        break
    else:
        print("숫자만 입력해주세요")
