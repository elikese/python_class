class Map:
    def __init__(self, size, goal, obstacles):
        self.size = size
        self.goal = goal
        self.obstacles = obstacles

    def display(self, player_pos):
        for y in range(self.size):
            for x in range(self.size):
                coord = (x, y)
                if coord == player_pos:
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
        if not (0 <= x < self.size and 0 <= y < self.size):
            print("맵 밖으로는 이동할 수 없습니다.")
            return False

        if coord in self.obstacles:
            print("장애물이 있어 이동할 수 없습니다.")
            return False

        return True
