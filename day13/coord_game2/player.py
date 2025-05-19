class Player:
    def __init__(self, start_position, hp=100):
        self.position = start_position
        self.hp = hp

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
        return self.position

    def attack(self, enemy):
        print("🗡️ 플레이어가 적을 공격! 20 데미지!")
        enemy.hp -= 20
