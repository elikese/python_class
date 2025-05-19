# 이중 for문 복습

for y in range(5):  # 바깥쪽 -> 세로
    for x in range(5):  # 안쪽 -> 가로
        print(".", end=" ")
    print()
print("--------------")
# y는 아래로 갈때 +
# x는 오른쪽으로 갈때 +

# (2,2)에 "." 말고 C라고 보이게 하려면 어떻게?
for y in range(5):  # 바깥쪽 -> 세로
    for x in range(5):  # 안쪽 -> 가로
        if (x, y) == (2, 2):
            print("C", end=" ")
        else:
            print(".", end=" ")
    print()

# 이걸 좌표로 이동하는 게임을 한번 만들어 봅시다
목표좌표 = (4, 4)  # G : goal
플레이어좌표 = (0, 0)  # P : player
print("--------------")
for y in range(5):
    for x in range(5):
        if (x, y) == 목표좌표:
            print("G", end=" ")
        elif (x, y) == 플레이어좌표:
            print("P", end=" ")
        else:
            print(".", end=" ")
    print()

# 0. 좌표 및 맵 설정을 한다(이중 for문)
# 1. input()을 통해서 wasd 중 하나를 입력을 받는다.
# 2. 입력을 받으면, 검증(5x5 지도 안에 있는지) 을 한다.
# 3. 검증이 되면, 이동할 좌표를 플레이어좌표에 대입한다.
# 4. 바뀐좌표를 기준으로 다시 이중 for문을 통해 맵을 출력한다.
# 5. 1 ~ 4를 계속 반복(while문)
# 6. P의 좌표가 G의 좌표와 같아지면 게임종료(break로 탈출)

플레이어좌표 = (0, 0)
맵사이즈 = 5

목표좌표 = (맵사이즈 - 1, 맵사이즈 - 1)
장애물좌표들 = [(1, 0), (2, 2), (3, 1)]
print("=== 좌표 이동 게임: G에 도달하세요! ===")
print("명령어: w(↑), s(↓), a_pakage(←), d(→), q(종료)")

while True:
    # 0. 좌표 및 맵 설정을 한다(이중 for문)
    for y in range(맵사이즈):  # y축 - 아래(+)
        for x in range(맵사이즈):  # x축 - 오른쪽(+)
            if (x, y) == 플레이어좌표:
                print("P", end=" ")
            elif (x, y) == 목표좌표:
                print("G", end=" ")
            elif (x, y) in 장애물좌표들:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

    # 6. P의 좌표가 G의 좌표와 같아지면 게임종료(break로 탈출)
    if 플레이어좌표 == 목표좌표:
        print("목표 지점에 도착했습니다! 게임 클리어!")
        break

    # 1. input()을 통해서 wasd 중 하나를 입력을 받는다.
    입력 = input("이동 >> ")

    # 입력받은 값을 바로 플레이어 좌표에 대입하기 전에, 검증해야한다!
    # 임시좌표를 만들어서 임시좌표를 검증하고, 검증이 되면, 임시좌표를 플레이어좌표로 다시 대입
    임시x, 임시y = 플레이어좌표

    if 입력 == "q":
        print("게임 종료!")
        break
    elif 입력 == "w":
        임시y -= 1
    elif 입력 == "s":
        임시y += 1
    elif 입력 == "a_pakage":
        임시x -= 1
    elif 입력 == "d":
        임시x += 1
    else:
        print("잘못된 입력입니다.")
        continue

    # 2. 입력을 받으면, 검증(5x5 지도 안에 있는지) 을 한다.
    if 임시x < 0 or 임시y < 0 or 임시x >= 맵사이즈 or 임시y >= 맵사이즈:
        print("맵 밖으로는 이동할 수 없습니다.")
        continue

    # 장애물 체크
    if (임시x, 임시y) in 장애물좌표들:
        print("장애물이 있어 이동할 수 없습니다.")
        continue

    # 3. 검증이 되면, 이동할 좌표를 플레이어좌표에 대입한다.
    플레이어좌표 = (임시x, 임시y)
