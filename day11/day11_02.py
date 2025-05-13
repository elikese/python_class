# class
# 클래스의 쉬운 설명 : 새로운 자료형을 정의 하는 것 (나만의 자료형)

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


# 생성자들 통해서 객체(인스턴스)를 생성할 수 있다.
puppy1 = Puppy("초코", 5)
puppy2 = Puppy("뽀삐", 5)

# 객체가 내부에 정의된 함수를 호출하면 자동으로 자기자신에 대한 데이터를
# self 변수에 담아서 호출한다.
# self를 전달 안해도 알아서 해준다
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

"""
테트리스 게임 아시죠?
테트리스게임에서 여러 조각들이 존재합니다
긴막대기, ㄴ자, ㄱ자 등등
조각에도 유형이 있죠? 그 유형들로 최대한 직사각형에 끼워넣습니다

자료형이라고 하는거.
우리가 지금 만들고 쓰려고하는 클래스라는거
이것도 똑같습니다
자료형은 이미 파이썬에서 만들어놓은 조각모양이구요
클래스라는건 우리가 직접 정의하는 조각모양인거에요

그리고 그걸 생성하면 실제로 메모리에 띄우는거에요
조각모양이라는건 아직 논리적개념, 즉 이렇게 생겼어~ 라고하는 모양(틀)일 뿐이지
진짜 생성되야 메모리에 적재할 수 있는거잖아요

조각모양이 바로 클래스이구요
생성되서 메모리에 적재되는게 인스턴스(객체)
"""

class Person:
    def __init__(self, name):
        self.name = name


man1 = Person("철수")
man2 = Person("철수")

print(man1 == man2)

# __init__() < 설명 x 다음 시차에..
# self 가 뭐지?

print(id(man1))  # id() 메모리 주소를 10진수로 변환해서 알려줍니다
print(id(man2))  # 메모리주소는 16진수 0x00014B7C1

puppy_memory_address = Person.__new__(Person)
print(puppy_memory_address)

Person.__init__(puppy_memory_address, "영희")
print(puppy_memory_address.name)
