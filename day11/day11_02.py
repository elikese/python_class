# class
# 클래스는 내가 스스로 자료형을 정의 하는 것 (나만의 자료형)

a = 10
b = "abc"
print(type(a))  # int 자료형
print(type(b))  # str 자료형

print(b.upper())  # str 자료형에는 여러 함수(메서드)가 존재 한다

# 클래스란? 내가 정의하는 데이터형식(자료형) + 동작(함수)를 묶은 것


class Puppy:
    # 클래스는 첫글자 대문자(PascalCase)
    # __init__(self, 내가 이 클래스에 정의하고싶은 자료들) : 생성자
    # self.자료1 = 매개변수
    # self.자료2 = 매개변수
    # self -> 생성된 자기 자신을 의미
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name}가 생성되었어요")

    def bark(self):
        print(f"{self.name}가 짖습니다. 왈왈")


puppy1 = Puppy("꼬맹이", 5)
puppy2 = Puppy("뭉치", 5)

puppy1.bark()
puppy2.bark()

# 실습
# Cat class 만들어 주세요
# Cat class는 name과 age 속성을 가지고 있습니다.
# class 내에 meow 함수 만들어 주세요
# 서로 다른 2마리 고양이 만들어서 각각 meow 호출 해 주세요


class Cat:
    def __init__(self, name, age=5):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name}이 웁니다 미야옹~")


cat1 = Cat("고영희", 5)
cat2 = Cat("고얌희", 5)

cat1.meow()
cat2.meow()

# Class는 결국에 설계도(틀) 누군가는 클래스를 붕어빵 틀이라고 표현합니다
# Class를 통해 만든 붕어빵은 붕어빵 틀하고는 다른거죠
# 똑같이 생긴 붕어빵도 사실 서로 다른 붕어빵

dolly = Puppy("돌리", 10)
dolly2 = Puppy("돌리", 10)

print(dolly == dolly2)

# __init__() < 설명 x 다음 시차에..
# self 가 뭐지?

print(id(dolly))  # id() 메모리 주소를 10진수로 변환해서 알려줍니다
print(id(dolly2))  # 메모리주소는 16진수 0x00014B7C1

puppy_memory_address = Puppy.__new__(Puppy)
print(puppy_memory_address)

Puppy.__init__(puppy_memory_address, "삐삐", 5)
print(puppy_memory_address.name, puppy_memory_address.age)
