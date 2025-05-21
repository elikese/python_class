from map import Map
from player import Player


class CoordGame:
    def __init__(self, map_size, player_start, goal, obstacles):
        self.map = Map(map_size, goal, obstacles)
        self.player = Player(player_start)

    def run(self):
        print("=== 좌표 이동 게임: G에 도달하세요! ===")
        print("명령어: w(↑), s(↓), a(←), d(→), q(종료)")

        while True:
            self.map.display(self.player.position)

            if self.player.position == self.map.goal:
                print("목표 지점에 도착했습니다! 게임 클리어!")
                break

            command = input("이동(w,a,s,d)입력 >> ")
            new_coord = self.player.move(command)

            if new_coord is None:
                print("잘못된 입력입니다.")
                continue

            if self.map.is_valid_move(new_coord):
                self.player.position = new_coord
