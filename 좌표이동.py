import sys

x = 0
y = 4
SIZE = 10

goal_x = 9
goal_y = 9

# 장애물 좌표 리스트
obstacles = [(1, 0), (2, 2), (3, 1)]
print("=== 좌표 이동 게임: G에 도달하세요! ===")
print("명령어: w(↑), s(↓), a(←), d(→), q(종료)\n")

while True:
    # 맵 출력
    for j in range(SIZE):
        for i in range(SIZE):
            if (i, j) == (x, y):
                print("P", end=" ")
            elif (i, j) == (goal_x, goal_y):
                print("G", end=" ")
            elif (i, j) in obstacles:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

    # 목표 도달 여부 확인
    if (x, y) == (goal_x, goal_y):
        print("🎉 목표 지점에 도착했습니다! 게임 클리어!")
        break

    # 입력
    cmd = input("이동 >> ")

    # 이동 처리
    new_x = x
    new_y = y

    if cmd == "q":
        print("게임 종료!")
        break
    elif cmd == "w":
        new_y -= 1
    elif cmd == "s":
        new_y += 1
    elif cmd == "a":
        new_x -= 1
    elif cmd == "d":
        new_x += 1
    else:
        print("잘못된 입력입니다.")
        continue

    # 경계 체크
    if new_x < 0 or new_x >= SIZE or new_y < 0 or new_y >= SIZE:
        print("❌ 맵 밖으로는 이동할 수 없습니다.")
        continue

    # 장애물 체크
    if (new_x, new_y) in obstacles:
        print("🚧 장애물이 있어 이동할 수 없습니다.")
        continue

    # 이동 확정
    x = new_x
    y = new_y
