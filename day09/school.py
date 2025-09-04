# 🎓 학생 관리 시스템 (전역 변수 방식)

학생목록 = []


def 학생등록():
    이름 = input("이름 >> ")
    학번 = input("학번 >> ")
    전공 = input("전공 >> ")

    # 중복 학번 방지
    for s in 학생목록:
        if s["학번"] == 학번:
            print("이미 존재하는 학번입니다. 등록 취소")
            return

    새학생 = {"이름": 이름, "학번": 학번, "전공": 전공}
    학생목록.append(새학생)
    print(f"등록 완료: {이름} / {학번} / {전공}")


def 학생목록보기():
    if not 학생목록:
        print("⚠️ 등록된 학생이 없습니다.")
        return False
    print("\n[전체 학생 목록]")
    for idx in range(len(학생목록)):
        s = 학생목록[idx]
        print(f"{idx+1}. 이름:{s['이름']} | 학번:{s['학번']} | 전공:{s['전공']}")


def 학생삭제():
    if not 학생목록보기():
        return

    대상이름 = input("삭제(퇴학)할 학생의 이름 >> ").strip()
    for s in 학생목록:
        if s["이름"] == 대상이름:
            학생목록.remove(s)
            print(f"'{대상이름}' 학생을 삭제했습니다.")
            return

    print("해당 이름의 학생을 찾을 수 없습니다.")


# 메인 루프
while True:
    print("\n===== 학생 관리 시스템 =====")
    print("1. 학생 등록")
    print("2. 전체 학생 보기")
    print("3. 학생 삭제(이름 기준)")
    print("4. 종료")
    선택 = input("메뉴 번호 >> ").strip()

    if 선택 == "1":
        학생등록()
    elif 선택 == "2":
        학생목록보기()
    elif 선택 == "3":
        학생삭제()
    elif 선택 == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 1~4 중에서 선택하세요.")
