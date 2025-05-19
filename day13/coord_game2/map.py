class Map:
    def __init__(self, size, enemies):
        self.size = size
        self.enemies = enemies

    def is_valid(self, position):
        x, y = position
        return 0 <= x < self.size and 0 <= y < self.size

    def get_enemy(self, position):
        for enemy in self.enemies:
            if enemy.position == position and enemy.is_alive():
                return enemy
        return None

    def print_map(self, player, goal):
        for y in range(self.size):
            for x in range(self.size):
                if (x, y) == player.position:
                    print("P", end=" ")
                elif (x, y) == goal:
                    print("G", end=" ")
                elif any(
                    enemy.position == (x, y) and enemy.is_alive()
                    for enemy in self.enemies
                ):
                    print("E", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

    def occupied_positions(self, player):
        positions = [player.position]
        positions += [e.position for e in self.enemies if e.is_alive()]
        return set(positions)
