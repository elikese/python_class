# 실제 생성자 작동 순서
# __new__(객체 메모리를 만듦) -> __init__(그 메모리에 데이터 넣음)
# __new__를 오버라이딩하면, 실제 생성되는 객체의 메모리를 직접 조작


class BankAccount:
    bank_name = "농협"
    clients = []
    count = 0
    max_clients_num = 2

    def __new__(cls, **info):
        if cls.count >= cls.max_clients_num:
            print("현재 계좌는 개설이 불가능합니다")
            return None

        memory_address = super().__new__(cls)
        return memory_address

    def __init__(self, **info):
        self.name = info.get("name")
        self.balance = info.get("balance")
        BankAccount.count += 1
        BankAccount.clients.append(self)

    def transfer(self, opponent_name, amount):
        if amount > self.balance:
            print("잔액이 부족합니다")
            return

        for client in BankAccount.clients:
            if client.name == opponent_name:
                client.balance += amount
                self.balance -= amount

    def print_balance(self):
        print(self.balance)


홍길동계좌 = BankAccount(name="홍길동", balance=100000)
고길동계좌 = BankAccount(name="고길동", balance=50000)
고길동계좌2 = BankAccount(name="고길동2", balance=50000)

홍길동계좌.transfer("고길동", 30000)
홍길동계좌.print_balance()
고길동계좌.print_balance()


# 클래스 메서드 @classmethod
# 정적 메서드 @staticmethod


class Person:
    # 클래스 변수 : 모든 Person의 인스턴스(객체)가 접근가능
    # 클래스로도 접근가능한 변수
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    def print_person(self):  # 인스턴스 메서드: 인스턴스만 호출가능
        print(f"이름: {self.name}, 나이: {self.age}")

    @classmethod
    def print_population(cls):  # 클래스 메소드: 클래스와 인스턴스 모두 호출가능
        print(f"현재 인구수: {cls.population}")
        return cls.population

    @classmethod
    def from_dict(cls, person_dict):
        return cls(person_dict.get("name"), person_dict.get("age"))

    @staticmethod
    def is_adult(age):  # 스태틱 메소드: 클래스와 인스턴스 모두 호출가능
        return age > 18


person1 = Person("홍길동", 20)
person2 = Person("고길동", 30)

person1.print_person()  # 인스턴스 메서드 호출가능
result1 = person1.print_population()
result2 = Person.print_population()
print(id(result1), id(result2))  # 주소가 동일하다

"""
인스턴스 메서드 -> self를 무조건 받는다 ->  인스턴스를 조작할 때 사용(객체 속성 값 조작)
클래스 메서드 -> cls를 무조건 받는다 -> 클래스를 조작할 떄 사용(클래스 조작)
스태틱 메서드 -> 일반적인 함수랑 동일 -> 그 클래스에서 자주 쓰일 것 같은 유틸함수(도우미)
"""

dict_person = {"name": "김철수", "age": 25}
person3 = Person(dict_person.get("name"), dict_person.get("age"))
person4 = Person.from_dict(dict_person)
person3.print_person()
person4.print_person()
Person.print_population()
