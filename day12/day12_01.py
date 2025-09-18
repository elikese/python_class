# 저번 시간 복습
# 클래스! : 붕어빵 틀(구멍을 뚫어놓고, 사용하는 양식같은 것)
class Puppy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}가 짖습니다 멍멍")


# 객체(인스턴스)를 생성 가능
puppy1 = Puppy("뽀삐", 5)
puppy2 = Puppy("삐삐", 4)

# 각 인스턴스의 속성마다 다른 결과가 나온다
puppy1.bark()
puppy2.bark()

# 각 인스턴스의 메모리 주소는 서로 다르다
print(id(puppy1))
print(id(puppy2))

print(puppy1 is puppy2)  # false


# 클래스 변수
# __init__()을 통해서 만들어주는 name, age와 같은 속성들
# 인스턴스 변수라고 한다. -> 각 인스턴스는 개별적인 인스턴스 변수값을 가지는 것.
# 비유
# 인스턴스 변수는 각 개인의 데이터를 보관하는 사물함
# 클래스 변수는 공용의 데이터를 보관하는 사물함
# 공용 -> 모든 인스턴스가 접근이 가능. (참고: 클래스로도 접근이 가능)


class BankAccount:
    bank_name = "농협"
    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        BankAccount.count += 1  # 질문가능성 있음


# 질문가능성
# class 안의 함수는 클래스 변수를 참조할 수 없음
# 함수안의 함수 -> 하위함수가 상위함수의 변수를 참조 할 수 있음
# 어려운 설명 : class는 dict기반으로 만들어진 type의 인스턴스이다.
# 대신 이걸 이해하려면 class또한 객체라는 이해가 있어야 함.

홍길동계좌 = BankAccount("홍길동", 10000)
고길동계좌 = BankAccount("고길동", 10000)

bank_name1 = 홍길동계좌.bank_name
bank_name2 = 고길동계좌.bank_name
bank_name3 = BankAccount.bank_name

print(bank_name1, bank_name2)  # 같은 값
print(bank_name1 == bank_name2)  # 같은 메모리주소를 공유하는 거구나
print(bank_name1 == bank_name3)  # 같은 메모리주소를 공유하는 거구나

print(f"현재 개설된 계좌수: {BankAccount.count}")

# 변경하려면 클래스로 참조해서 변경해야한다
BankAccount.bank_name = "신한"
print(BankAccount.bank_name)


# 실습
class Student:
    """
    학생 클래스 연습용

    요구사항:
    1. 모든 학생은 같은 학교에 다님 (클래스 변수)
    2. 학생이 만들어질 때마다 총 학생 수 카운트 (클래스 변수)
    3. 각 학생마다 이름이 다름 (인스턴스 변수)
    """

    # TODO: 여기에 클래스 변수 2개를 만드세요
    # 힌트: school = "?" , student_count = ?

    def __init__(self, name):
        # TODO: 학생 이름을 저장하세요 (self.name = ?)
        # TODO: 학생 수를 1 증가시키세요 (Student.student_count += 1)
        pass

    def introduce(self):
        # TODO: "안녕하세요, 저는 {이름}입니다. {학교}에 다닙니다." 출력하세요
        pass


# 상속
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(f"{self.name}가 밥을 먹습니다")
#
#     def sound(self):
#         print("멍멍")
#
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(f"{self.name}가 밥을 먹습니다")
#
#     def sound(self):
#         print("야옹")


# Dog와 Cat class의 중복이 많다 -> 공통점을 추려서 상위 클래스를 정의


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}가 밥을 먹습니다")


class Dog(Pet):
    def sound(self):
        print("멍멍")


class Cat(Pet):
    def sound(self):
        print("야옹")


# Dog와 Cat이 Pet을 상속한 상태
# Dog와 Cat은 __init__ 정의 x, eat 정의하지 x

# 정의하지 않아도, 부모의 __init__을 호출할 수 있다
dog = Dog("뽀삐", 5)
cat = Cat("삐삐", 5)

# 정의하지 않아도, 부모의 eat을 호출할 수 있다
dog.eat()
cat.eat()


# dog는 Dog class의 인스턴스
# Dog class에는 지금 eat이라는 함수는 정의 되지 않았다.
# Dog class에 eat함수가 없으면 -> 부모에 eat이라는 함수가 있나? -> 있으면 부모의 eat을 호출
# __init__도 마찮가지로, Dog class의 __init__이 없으면
# -> 부모에 있는지 찾아보고 있으면 호출

# 고급진 말로 MRO : method resolution order
