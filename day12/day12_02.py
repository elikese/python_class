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

