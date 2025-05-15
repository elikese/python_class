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


# drive라는 같은 메서드 -> 다른 동작 : 다형성(polymorphism)
# 왜 이런걸 하나요?? 기능을 정의하는것(부모): 달린다 / 구체적인 기능을 구현하는걸(자식) 분리
test_car(e_car)
test_car(gas_car)

# payment를 함수의 조합으로 구현 -> 함수가 함수를 매개변수로 받아서 사용하는 특징을 사용


def order(payment, *menu_names):
    menu = {
        "피자": 25000,
        "치킨": 20000,
    }
    price = 0
    for menu_name in menu_names:
        price += menu[menu_name]

    final_price = payment(price)
    print(f"총 결제금액: {final_price}")


def kakao_payment(price):
    # 항상 10프로 할인
    return price * 0.9


def naver_payment(price):
    # 주문금액 20000원 이상이면 2000원 할인
    if price >= 20000:
        return price - 2000

    return price


# 함수에 함수를 전달해서, 구체적인 기능구현을 분리
order(naver_payment, "피자", "치킨")


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
