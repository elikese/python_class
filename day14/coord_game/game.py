class CoordGame:
    def __init__(self, map_instance, player_instance):
        self.map = map_instance
        self.player = player_instance

    def run(self):
        print("=== 좌표 이동 게임: G에 도달하세요! ===")
        print("명령어: w(위), s(아래), a(좌), d(우), q(종료)")

        while True:
            self.map.paint_map(self.player.position)

            if self.player.position == self.map.goal:
                print("목표 지점에 도착했습니다! 게임 클리어!")
                break

            command = input("이동(w,a,s,d)입력, 종료(q) >> ")

            if command == "q":
                print("게임 종료")
                break

            new_coord = self.player.move(command)

            if new_coord is None:
                print("잘못된 입력입니다.")
                continue

            if self.map.is_valid_move(new_coord):
                self.player.position = new_coord
