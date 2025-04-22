import random

주사위 = 0

while 주사위 != 6:
    주사위 = random.randint(1, 6)
    print(f"주사위 눈금: {주사위}")

print("6이 나왔습니다! 게임 끝!")
