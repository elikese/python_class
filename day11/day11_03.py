dict_car1 = {"model": "소나타", "color": "흰색", "year": 2020}
dict_car2 = {"model": "아반떼", "color": "검은색", "year": 2019}


def print_car(dict):
    print(f"모델명:{dict['model']}, 색상:{dict['color']}, 연식:{dict['year']}")


class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def print_car(self):
        print(f"모델명:{self.model}, 색상:{self.color}, 연식:{self.year}")


car1 = Car("소나타", "흰색", 2020)
car2 = Car("아반떼", "검은색", 2019)
# dict는 좀 더 유연합니다. (메모지에 쓴것)
# class는 (데이터를 설계자가 만든 양식에 기입하는 것) + 함수(메서드) 존재
# 양식이 통일됬을때의 장점들.

car1.print_car()
car2.print_car()

# 속성을 변경하려면?
car1.color = "파란색"
car1.print_car()


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족")
        else:
            self.balance -= amount

    def check_balance(self):
        print(f"{self.name}의 잔액: {self.balance}원")


acc = BankAccount("철수", 10000)
acc.deposit(3000)
acc.withdraw(5000)
acc.check_balance()


# isinstance(instance자리,class자리) :

# str, 숫자(int, float), list -> Class
a = 10
print(type(a))  # a의 instance의 클래스를 보여줌
print(isinstance(a, int))


# 시험성적표
class TestScore:

    # 성적이 100보다 크거나 0보다 작을 수 있습니까?
    # 성적이 int 인스턴스 여야하죠?
    def __init__(self, name, kor, eng, math):
        # if not isinstance(kor, int):
        #     print("점수는 숫자여야 합니다")
        #     return
        #
        # if kor > 100 or eng > 100 or math > 100:
        #     print("100보다 큰 수는 올 수 없습니다")
        #     return
        #
        # if kor < 0 or eng < 0 or math < 0:
        #     print("0보다 작은 수는 올 수 없습니다")
        #     return

        for score in [kor, eng, math]:
            if not isinstance(score, int):
                print("점수는 숫자여야 합니다")
                return
            if score > 100:
                print("100보다 큰 수는 올 수 없습니다")
                return
            if score < 0:
                print("0보다 작은 수는 올 수 없습니다")
                return

        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


철수성적표 = TestScore("철수", 80, 70, 90)
영희성적표 = TestScore("영희", 75, 85, 100)
이상한성적표 = TestScore("이상한", -100, 120, 90)

# 점수 평균을 구하는 함수를 클래스 내부에 만들어서 평균을 구해주세요
# def get_avarage(self):


class Cup:
    def __init__(self, size):
        self.size = size
        self.water = 0

    def check(self):
        print(f"현재 물: {self.water}ml / 최대 용량: {self.size}ml")

    def fill(self, amount):
        if self.water + amount > self.size:
            print("물이 넘칩니다!")
            return

        self.water += amount
        print(f"{amount}ml 물을 채웠습니다. 현재 {self.water}ml")

    def drink(self, amount):
        if self.water - amount < 0:
            print("물이 부족합니다!")
            return

        self.water -= amount
        print(f"{amount}ml 물을 마셨습니다. 현재 {self.water}ml")


# drink(self, amount):
# 1. 현재 water와 amount를 비교해서 용량이 충분한지 검사 하는 코드
# 2. 검사를 통과하면, water를 감소시키고, 현재 남은 water도 같이 출력해주세요
