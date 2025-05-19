class Enemy:
    def __init__(self, position, hp=30, damage=10):
        self.position = position
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def attack(self, player):
        print(f"💥 적이 공격! 플레이어에게 {self.damage} 데미지")
        player.hp -= self.damage

    def to_dict(self):
        return {"position": self.position, "hp": self.hp, "damage": self.damage}

    @classmethod
    def from_dict(cls, data):
        return cls(tuple(data["position"]), data["hp"], data["damage"])
