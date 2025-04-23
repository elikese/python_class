player_x, player_y = 0, 0
SIZE = 5

goal_x, goal_y = (4, 4)
obstacles = [(1, 0), (2, 2), (3, 1)]
print("=== 좌표 이동 게임: G에 도달하세요! ===")
print("명령어: w(↑), s(↓), a(←), d(→), q(종료)")

while True:
    # 맵 출력
    for j in range(SIZE):  # y축
        for i in range(SIZE):  # x축
            if (i, j) == (player_x, player_y):
                print("P", end=" ")
            elif (i, j) == (goal_x, goal_y):
                print("G", end=" ")
            elif (i, j) in obstacles:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

    # 목표 도달 여부 확인
    if (player_x, player_y) == (goal_x, goal_y):
        print(" 목표 지점에 도착했습니다! 게임 클리어!")
        break

    # 입력
    cmd = input("이동 >> ")

    # 이동 처리
    temp_x = player_x
    temp_y = player_y

    if cmd == "q":
        print("게임 종료!")
        break
    elif cmd == "w":
        temp_y -= 1
    elif cmd == "s":
        temp_y += 1
    elif cmd == "a":
        temp_x -= 1
    elif cmd == "d":
        temp_x += 1
    else:
        print("잘못된 입력입니다.")
        continue

    # 경계 체크
    if temp_x < 0 or temp_x >= SIZE or temp_y < 0 or temp_y >= SIZE:
        print("맵 밖으로는 이동할 수 없습니다.")
        continue

    # 장애물 체크
    if (temp_x, temp_y) in obstacles:
        print("장애물이 있어 이동할 수 없습니다.")
        continue

    # 이동 확정
    player_x = temp_x
    player_y = temp_y
