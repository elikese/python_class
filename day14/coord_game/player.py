class Player:
    def __init__(self, start_pos):
        self.position = start_pos

    def move(self, direction):
        x, y = self.position
        if direction == "w":
            return (x, y - 1)
        elif direction == "s":
            return (x, y + 1)
        elif direction == "a":
            return (x - 1, y)
        elif direction == "d":
            return (x + 1, y)
        elif direction == "q":
            exit("게임 종료")
        return None
