class Character:
    def __init__(self, nick_name):
        self.nick_name = nick_name
        self.HP = 100

    def attack(self, opponent):
        dmg = 10
        print(f"{opponent.nick_name}을 기본 공격({dmg})합니다")
        opponent.HP -= 10


class Warrior(Character):
    def attack(self, opponent: Character):
        dmg = 15
        print(f"{self.nick_name} → {opponent.nick_name}: 검공격({dmg}) ⚔️")
        opponent.HP -= dmg


class Mage(Character):
    def attack(self, opponent: Character):
        dmg = 20
        print(f"{self.nick_name} → {opponent.nick_name}: 파이어볼({dmg})")
        opponent.HP -= dmg


import random
import time


def battle(char1, char2):
    print(f"전투시작! {char1.nick_name} vs {char2.nick_name}")

    while True:
        if char1.HP <= 0 or char2.HP <= 0:
            break

        input(">>>엔터를 눌러 주사위를 굴립니다")
        dice = random.randint(1, 6)
        is_even = dice % 2 == 0

        attacker = char2 if is_even else char1
        defender = char1 if is_even else char2
        attacker, defender = (char1, char2) if is_even else (char2, char1)

        print(
            f"{dice} -> {'짝수' if is_even else '홀수'} -> {attacker.nick_name}의 턴!!"
        )
        time.sleep(0.5)
        attacker.attack(defender)
        time.sleep(0.5)
        print("====현재 상황====")
        print(
            f"{attacker.nick_name}의 체력:{attacker.HP}, {defender.nick_name}의 체력:{defender.HP}"
        )

        if defender.HP <= 0:
            print(f"{attacker.nick_name} 승리!")


char1 = Warrior("타락파워전사")
char2 = Mage("썬콜")
battle(char1, char2)
