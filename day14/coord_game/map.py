class Map:
    def __init__(self, **options):
        self.size = options.get("size")
        self.goal = options.get("goal")
        self.obstacles = options.get("obstacles")

    def paint_map(self, player_position):
        for y in range(self.size):
            for x in range(self.size):
                coord = (x, y)
                if coord == player_position:
                    print("P", end=" ")
                elif coord == self.goal:
                    print("G", end=" ")
                elif coord in self.obstacles:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print()

    def is_valid_move(self, coord):
        x, y = coord
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            print("맵 밖으로는 이동할 수 없습니다.")
            return False

        if coord in self.obstacles:
            print("장애물이 있어 이동할 수 없습니다.")
            return False

        return True
