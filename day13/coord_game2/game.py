from map import Map
from player import Player
from enemy import Enemy


class Game:
    def __init__(self, size, player_pos, goal, enemy_data, max_moves=50):
        self.player = Player(player_pos)
        self.goal = goal
        self.map = Map(size, [Enemy(pos, hp, dmg) for pos, hp, dmg in enemy_data])
        self.max_moves = max_moves
        self.move_count = 0

    def run(self):
        print("🎮 게임 시작! 목표 지점(G)에 도달하세요!")
        while True:
            self.map.print_map(self.player, self.goal)
            print(f"HP: {self.player.hp}, 이동: {self.move_count}/{self.max_moves}")

            if self.player.position == self.goal:
                print("🎉 클리어!")
                break
            if self.player.hp <= 0:
                print("💀 사망!")
                break
            if self.move_count >= self.max_moves:
                print("⛔ 이동 초과!")
                break

            cmd = input(">> ").strip().lower()
            if cmd == "q":
                break

            new_pos = self.player.move(cmd)
            if not self.map.is_valid(new_pos):
                print("❌ 맵 밖입니다.")
                continue

            enemy = self.map.get_enemy(new_pos)
            if enemy:
                enemy.attack(self.player)
                self.player.attack(enemy)
                if not enemy.is_alive():
                    print("💀 적 제거")
            else:
                self.player.position = new_pos

            self.move_count += 1
