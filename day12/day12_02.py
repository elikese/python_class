# 이러한 특성을 활용하면, 오버라이딩을 할 수 있다.
# 오버라이드는 부모의 메서드를 자식이 재정의


class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def drive(self):
        print(f"{self.name}가 달립니다")


class ElectricCar(Car):
    def __init__(self, name, model, battery):
        super().__init__(name, model)  # super(): 부모의 메서드 연결해주는 함수
        self.battery = battery

    def drive(self):
        super().drive()
        print("전기로")


class GasolineCar(Car):

    def __init__(self, name, model, gas):
        super().__init__(name, model)
        self.gas = gas

    def drive(self):
        super().drive()
        print("가스로")


e_car = ElectricCar("모델y", "tesla", 60)
gas_car = GasolineCar("x3", "BMW", 40)

e_car.drive()
gas_car.drive()


# Car를 상속한 ElectricCar / GasolineCar는
# __init__ / drive를 오버라이드 했다.


def test_car(car):
    car.drive()


print(isinstance(e_car, Car))
print(isinstance(gas_car, Car))

# drive라는 같은 메서드 -> 다른 동작 : 다형성(polymorphism)
# 왜 이런걸 하나요?? 기능을 정의하는것(부모): 달린다 / 구체적인 기능을 구현하는걸(자식) 분리
test_car(e_car)
test_car(gas_car)


class Payment:
    def __init__(self):
        print("결제 시스템 초기화")

    def pay(self, price):
        pass


class KakaoPayment(Payment):
    def pay(self, price):
        return price * 0.9  # 10% 할인


class NaverPayment(Payment):
    def pay(self, price):
        if price >= 20000:
            return price - 2000  # 2,000원 할인
        return price


def order(payment_instance, *menu_names):
    if not isinstance(payment_instance, Payment):
        print("올바른 결제방법을 선택하세요")
        return False

    menu = {
        "피자": 25000,
        "치킨": 20000,
    }
    price = 0
    for menu_name in menu_names:
        price += menu[menu_name]

    final_price = payment_instance.pay(price)
    print(f"총 결제금액: {final_price}")


kakao = KakaoPayment()
naver = NaverPayment()
order(kakao, "피자", "치킨")
order(naver, "피자", "치킨")


# 함수로 구현하고, 클래스로도 구현이 가능.


class Character:
    def __init__(self, nick_name):
        self.nick_name = nick_name
        self.HP = 100

    def attack(self, opponent):
        print(f"{opponent.nick_name}을 기본 공격(10)합니다")
        opponent.HP -= 10


# 실습) Character 클래스를 상속받는 Warrior(전사), Mage(마법사)를 구현
#  Warrior(전사)와 Mage(마법사) attack을 오버라이드해서
# 전사는 검으로 공격 / 마법사는 파이어 볼로 공격, 각각 데미지도 다르게 오버라이드 해보세요


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

    if not isinstance(char1, Character) or not isinstance(char2, Character):
        return

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

        print(f"{dice} -> {'짝수' if is_even else '홀수'} -> {attacker.nick_name}의 턴!!")
        time.sleep(0.5)
        attacker.attack(defender)
        time.sleep(0.5)
        print("====현재 상황====")
        print(f"{attacker.nick_name}의 체력:{attacker.HP}, {defender.nick_name}의 체력:{defender.HP}")

        if defender.HP <= 0:
            print(f"{attacker.nick_name} 승리!")


char1 = Warrior("타락파워전사")
char2 = Mage("썬콜")
battle(char1, char2)


# 상속을 통한 프로토타입 패턴
class Robot:
    """
    복잡한 로봇 클래스 (매개변수가 너무 많음)
    """

    def __init__(self, name, speed, power, color, size, voice, battery):
        self.name = name
        self.speed = speed  # 속도 (1-10)
        self.power = power  # 힘 (1-10)
        self.color = color  # 색깔
        self.size = size  # 크기 (small/medium/large)
        self.voice = voice  # 목소리 타입
        self.battery = battery  # 배터리 용량

        print(f"{name} 로봇 생성됨!")
        print(f"설정: 속도={speed}, 힘={power}, 색깔={color}")

    def move(self):
        print(f"{self.name}이 속도 {self.speed}로 움직입니다!")

    def work(self):
        print(f"{self.name}이 힘 {self.power}로 일합니다!")


# 문제: 매번 이렇게 긴 매개변수를 다 써야 함
# robot = Robot("테스트봇", 5, 7, "파란색", "medium", "기계음", 100)


class HomeRobot(Robot):
    """
    집안일용 로봇 - 이름만 정하면 됨
    (청소, 요리 등에 적합한 기본 설정)
    """

    def __init__(self, name):
        # 집안일용으로 최적화된 기본값 사용
        super().__init__(
            name=name,
            speed=3,  # 천천히 (안전하게)
            power=5,  # 적당한 힘
            color="흰색",  # 깔끔한 색
            size="medium",  # 적당한 크기
            voice="부드러운",  # 친근한 목소리
            battery=80,  # 하루 종일 사용 가능
        )


class WorkerRobot(Robot):
    """
    공장용 로봇 - 이름만 정하면 됨
    (무거운 일에 적합한 기본 설정)
    """

    def __init__(self, name):
        # 공장용으로 최적화된 기본값 사용
        super().__init__(
            name=name,
            speed=8,  # 빠르게
            power=10,  # 최대 힘
            color="노란색",  # 주의 색상
            size="large",  # 큰 크기
            voice="기계음",  # 명확한 음성
            battery=120,  # 장시간 작업 가능
        )
