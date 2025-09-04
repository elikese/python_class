# 📚 책 관리 프로그램 (함수 분리)

책목록 = []


def 책등록():
    이름 = input("책 이름을 입력하세요 >> ")
    저자 = input("저자를 입력하세요 >> ")
    책 = {"이름": 이름, "저자": 저자}
    책목록.append(책)
    print(f"✅ '{이름}'(저자: {저자}) 이 등록되었습니다.")


def 책보기():
    if not 책목록:
        print("⚠️ 등록된 책이 없습니다.")
        return False
    else:
        print("\n[전체 책 목록]")
        for idx in range(len(책목록)):
            책 = 책목록[idx]
            print(f"{idx+1}. {책['이름']} - {책['저자']}")


def 책대여():
    if not 책보기():
        return
    제목 = input("대여할 책 이름을 입력하세요 >> ")
    for 책 in 책목록:
        if 책["이름"] == 제목:
            책목록.remove(책)
            print(f"📕 '{제목}' 책이 대여(삭제)되었습니다.")
            return
    print("❌ 해당 책을 찾을 수 없습니다.")


# 메인 루프
while True:
    print("\n===== 📚 책 관리 프로그램 =====")
    print("1. 책 등록")
    print("2. 전체 책 보기")
    print("3. 책 대여(삭제)")
    print("4. 종료")
    선택 = input("메뉴 번호를 입력하세요 >> ")

    if 선택 == "1":
        책등록()
    elif 선택 == "2":
        책보기()
    elif 선택 == "3":
        책대여()
    elif 선택 == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("❌ 잘못된 입력입니다. 1~4 중에서 선택하세요.")
