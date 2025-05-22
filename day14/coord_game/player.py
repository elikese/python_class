class Player:
    def __init__(self, **options):
        self.position = options.get("start_position")

    def move(self, move_input):
        x, y = self.position
        if move_input == "w":
            return (x, y - 1)
        elif move_input == "s":
            return (x, y + 1)
        elif move_input == "a":
            return (x - 1, y)
        elif move_input == "d":
            return (x + 1, y)
        return None
