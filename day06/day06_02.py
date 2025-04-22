# 미니로또
# 6개 랜덤숫자(1~45사이 숫자들로)
# 6개 모두 맞으면 1등, 5개 -> 2등, 4개 -> 3등, 3개 이하 -> 꽝

import random

print(random.randint(1, 6))  # random.randint() # 1~6사이 랜덤숫자 생성
print(random.choice([1, 2, 3, 4, 5, 6]))  # 리스트중 무작위 하나 선택

당첨번호들 = []
while True:
    랜덤번호 = random.randint(1, 45)  # 1~45사이 랜덤숫자 생성
    if 랜덤번호 not in 당첨번호들:  # 중복 안된 숫자만 넣어줘야된다.
        당첨번호들.append(
            랜덤번호
        )  # 중복을 뽑게되면, 반복을 한번 더 해야하니 for문이 아니라 while쓴 겁니다.

    if len(당첨번호들) == 6:  # 최종적으로 6개를 뽑으면 탈출
        break
print(f"이번회차 당천범호들:{당첨번호들}")

내가찍은번호들 = []
while True:
    print(f"현재 뽑은번호들: {내가찍은번호들}")
    찍은번호 = input("1~45 사이 번호를 하나 찍어주세요 >>")
    if 찍은번호 not in 내가찍은번호들:
        내가찍은번호들.append(int(찍은번호))

    if len(내가찍은번호들) == 6:
        print(f"현재 뽑은번호들: {내가찍은번호들}")
        break

맞춘횟수 = 0
for 내가찍은번호 in 내가찍은번호들:
    if 내가찍은번호 in 당첨번호들:
        맞춘횟수 += 1

if 맞춘횟수 == 6:
    print("1등!")
elif 맞춘횟수 == 5:
    print("2등!")
elif 맞춘횟수 == 4:
    print("3등!")
else:
    print("꽝....")

# 실습) 숫자 업다운게임
# 추측이 정답보다 크면 print("다운!")
# 추측이 정답보다 작으면 print("업!")
# 정답을 맞출경우 정답숫자를 print하고 반복문 탈출!

정답숫자 = random.randint(1, 100)  # 1~100 사이
while True:
    추측숫자 = int(input("정답은 몇번일까요? 추측해서 입력해 보세요(1~100): "))
    if 추측숫자 > 정답숫자:
        print("다운!")
    elif 추측숫자 < 정답숫자:
        print("업!")
    else:
        print(f"정답입니다! {정답숫자}")
        break
