# 매직 메서드
# 모든 클래스의 공통 조상 -> object: 모든 클래스의 기본뼈대
# 매직 메서드 object의 메서드, 우리가 그걸 오버라이드 할 수 있다.
# __init__도 여태껏 우리가 object의 __init__을 오버리이드 한 것.
class Person(object):
    def __init__(self, name):  # 객체 초기화
        self.name = name
        self.age = 30

    def __str__(self):  # 문자열로 표현할 때 호출
        return self.name

    def __eq__(self, other):  # 비교연산(동등) 할 때 호출
        print("나이 비교")
        if isinstance(other, Person):
            return self.age == other.age
        elif isinstance(other, int):
            return self.age == other

    def __lt__(self, other):  # 비교연산(less than) 할 때 호출
        print("나이 비교")
        if isinstance(other, Person):
            return self.age < other.age
        elif isinstance(other, int):
            return self.age < other

    def __gt__(self, other):  # 비교연산(grater than) 할 때 호출
        print("나이 비교")
        if isinstance(other, Person):
            return self.age > other.age
        elif isinstance(other, int):
            return self.age > other

    def __le__(self, other):  # <= (less than or equal)
        if isinstance(other, Person):
            return self.age <= other.age
        elif isinstance(other, int):
            return self.age <= other

    def __ge__(self, other):  # >= (greater than or equal)
        if isinstance(other, Person):
            return self.age >= other.age
        elif isinstance(other, int):
            return self.age >= other

    def __add__(self, other):
        if isinstance(other, int):
            self.age += other
            return self
        return None

    def __sub__(self, other):
        if isinstance(other, int):
            self.age -= other
            return self
        return None

    def __mul__(self, other):
        if isinstance(other, int):
            self.age *= other
            return self
        return None

    def __truediv__(self, other):
        if isinstance(other, int):
            self.age /= other  # 또는 self.age = int(self.age / other)
            return self
        return None

person1 = Person("홍길동")
person2 = Person("홍길동")
print(person1)  # __str__ 호출
print(person1 == person2)  # __eq__ 호출
print(person1 > 10)  # __gt__ 호출
person1 + 5
print(person1.age)


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"현재좌표: ({self.x},{self.y})"

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    # __eq__ 구현: 각각의 x,y를 비교해서 같으면, true 리턴
    # __str__ 구현: 현재좌표: (x, y)

    # __add__ 구현: coord1 + coord2 -> 각각의 x,y가 더해지게 구현


"""
coord1 = Coord(1, 2)
coord2 = Coord(3, 4)
print(coord1 == coord2) # false 출력
print(coord1 + coord2) # 현재좌표: (4,6) 출력
print(coord1) # 현재좌표: (1,2) 출력
"""


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
        BankAccount.count += 1
        return memory_address

    def __init__(self, **info):
        self.name = info.get("name")
        self.balance = info.get("balance")
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


# 참고*))
# __new__()를 통해 객체 생성을 제한 할 수 있다.
# 생성자를 통해서 하나만 만들고 그것만 쓰게 만드는 패턴
# Singleton 패턴: 인스턴스 하나로만 쓰는 패턴


class Setting:
    instance_memory_address = None
    _initialized = False

    def __new__(cls, mode):
        if Setting.instance_memory_address is None:
            print("새 인스턴스 생성")
            Setting.instance_memory_address = super().__new__(cls)
        return Setting.instance_memory_address

    def __init__(self, mode):
        if not Setting._initialized:
            self.mode = mode
            Setting._initialized = True

    def print_mode(self):
        print(self.mode)


mode1 = Setting("light")
mode1.print_mode()
mode2 = Setting("dark")
mode1.print_mode() # 여전히 light 모드로 고정되어있다
