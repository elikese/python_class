def print_map(player, goal, map_size, obstacles):
    for y in range(map_size):
        for x in range(map_size):
            if (x, y) == player:
                print("P", end=" ")
            elif (x, y) == goal:
                print("G", end=" ")
            elif (x, y) in obstacles:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()


def apply_move(input_value, coord):
    (x, y) = coord
    if input_value == "w":
        return (x, y - 1)
    elif input_value == "s":
        return (x, y + 1)
    elif input_value == "a":
        return (x - 1, y)
    elif input_value == "d":
        return (x + 1, y)
    else:
        return "error"


def is_valid_move(coord, map_size, obstacles):
    x, y = coord
    if x < 0 or y < 0 or x >= map_size or y >= map_size:
        print("맵 밖으로는 이동할 수 없습니다.")
        return False
    if (x, y) in obstacles:
        print("장애물이 있어 이동할 수 없습니다.")
        return False
    return True


def coord_game(*, player, goal, map_size, obstacles):
    print("=== 좌표 이동 게임: G에 도달하세요! ===")
    print("명령어: w(↑), s(↓), a(←), d(→), q(종료)")

    while True:
        print_map(player, goal, map_size, obstacles)

        if player == goal:
            print("목표 지점에 도착했습니다! 게임 클리어!")
            break

        input_value = input("이동(w,a,s,d)입력 >> ")
        move_result = apply_move(input_value, player)

        if move_result == "error":
            print("잘못된 입력입니다.")
            continue

        if is_valid_move(move_result, map_size, obstacles):
            player = move_result


game_options = {
    "map_size": 5,
    "player": (0, 0),
    "goal": (4, 4),
    "obstacles": [(1, 0), (2, 2), (3, 1)],
}
# 실행
# 추가참고) def fn(*arg, a, b) -> a,b 는 호출할때 키워드로 a="", b="" 명시해줘야했다.
# 비슷한건데, def fn(*, a, b) -> a,b는 호출할때 키워드로 a="", b="" 명시해줘야한다.

coord_game(**game_options)
