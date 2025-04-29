import random
import time

print(random.randint(1, 6))  # random.randint() # 1~6사이 랜덤숫자 생성
print(random.choice([1, 2, 3, 4, 5, 6]))  # 리스트중 무작위 하나 선택

# 주사위
주사위 = 0
while 주사위 != 6:
    input("주사위를 굴리려면 엔터를 누르세요")
    주사위 = random.randint(1, 6)
    print(f"주사위 눈금: {주사위}")

print("6이 나왔습니다! 게임 끝!")

# (실습) 주사위 눈금과 시행횟수도 같이 보여주세요
주사위 = 0
while 주사위 != 6:
    input("주사위를 굴리려면 엔터를 누르세요")
    주사위 = random.randint(1, 6)
    print(f"주사위 눈금: {주사위}")

print("6이 나왔습니다! 게임 끝!")

# 실습) 숫자 업다운게임
# 추측이 정답보다 크면 print("다운!")
# 추측이 정답보다 작으면 print("업!")
# 정답을 맞출경우 정답숫자를 print하고 반복문 탈출!

정답번호 = random.randint(1, 50)  # 1~100 사이
while True:
    # int() 형변환 -> 문자를 입력했다면? 오류발생!
    # 오류 발생 후 처리 -> 오류처리
    # 오류 전에 검증 단계를 만들어서 사전에 처리
    예상번호 = input("정답은 몇번일까요? 추측해서 입력해 보세요(1~50): ")

    # str.isdigit() # 문자열이 숫자로만 이루어졌는가? 를 검증
    if not 예상번호.isdigit():
        print("숫자만 입력해주세요")
        continue
    형변환예상번호 = int(예상번호)

    # 1 ~ 50 사이인지 검증
    if 형변환예상번호 < 1 or 형변환예상번호 > 50:
        print("1~100사이 숫자를 입력해주세요")
        continue

    if 형변환예상번호 > 정답번호:
        print("다운!")
    elif 형변환예상번호 < 정답번호:
        print("업!")
    else:
        print(f"정답입니다! {정답번호}")
        break

# 가위바위보
가위바위보 = ["가위", "바위", "보"]
나의선택 = ""
컴퓨터선택 = ""
나의점수 = 0
컴퓨터점수 = 0

while True:
    if 나의점수 == 5:
        print("승리!")
        break
    elif 컴퓨터점수 == 5:
        print("컴퓨터 승리!")
        break

    나의선택 = input("가위, 바위, 보 중 선택 해 입력해 주세요.(종료하려면 q입력) >>")

    if 나의선택 not in 가위바위보 and 나의선택 != "q":
        print("가위, 바위, 보 중 하나를 입력해주세요")
        continue

    if 나의선택 == "q":
        print(f"게임끝! 컴퓨터 - {컴퓨터점수} 사용자 - {나의점수}")

    컴퓨터선택 = random.choice(가위바위보)

    print("과연 승부는", end="")
    for _ in range(5):
        print("..", end="")
        time.sleep(0.4)
    print()

    승리조건1 = 나의선택 == "가위" and 컴퓨터선택 == "보"
    승리조건2 = 나의선택 == "바위" and 컴퓨터선택 == "가위"
    승리조건3 = 나의선택 == "보" and 컴퓨터선택 == "바위"

    if 나의선택 == 컴퓨터선택:
        print("무승부!")
    elif 승리조건1 or 승리조건2 or 승리조건3:
        print("승리!")
        나의점수 += 1
    else:
        print("패배..")
        컴퓨터점수 += 1

    print(f"컴퓨터 - {컴퓨터점수} 사용자 - {나의점수}")
