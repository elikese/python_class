print("Hello world!")

# 변수
# 왜 사용하는가? 재사용, 가독성
# 변수는 이름표가 붙은 상자
# 데이터를 저장하기 위해 이름을 붙인 공간이다.

name = "박화목"
age = 33

# 기본 자료형
# int: 정수형 / float: 실수형 / str: 문자열 / bool: 불형(참,거짓)

pi = 3.14
isMale = True

print(type(name))
print(type(age))
print(type(pi))
print(type(isMale))

# 작명 방식 (Naming Convention)
# PascalCase -> PythonClass : 70년대에 Pascal언어를 쓸때 쓰던 방식
# camelCase -> pythonClass : 처음 끝은 평평한데 중간이 튀어나온게 마치 낙타의 혹같아서
# snake_case -> python_class : _ 모양이 마치 뱀이 기어가는 모양같아서
# 예약어 사용불가능 / _를 제외한 특수문자는 사용할 수 없다.

# input()
# input() 으로 저장한 변수의 자료형은 str이다.
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
print(name)
print(age)
print(name, age)
print("이름:", name, "나이:", age)

print("이름:" + name + "나이:" + age)
print(type(age)) # str age = "33" // "33" != 33


# 자기소개
# 이름(name), 나이(age)를 input으로 변수에 담아
# print()를 통해 "안녕하세요, 저는 박화목이고, 나이는 33살입니다." 출력
# 띄어쓰기 주의!
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")

sentence = "안녕하세요, 저는 " + name + "이고, 나이는 " + age + "살입니다."
print(sentence)

# 숫자자료형(int / float
num1 = 10
num2 = 20
num_sum = num1 + num2
print(num_sum)

fnum = 1.1
fnum2 = 0.1
fnum_sum = 1.1 + 0.1 # 1.2
print(fnum_sum == 1.2)
print(fnum_sum)

"""
왜 다른가?
컴퓨터는 2진수로 모든것을 이해한다.
1/10을 2진수로 최대한 근사하려고 한다.
1/10은 10^-1
1/16 + 1/32 + 1/256 + ........ => (무한소수)
무한하게 계산하지 않고, 특정 순간에 올림한다
=> 실제의 값보다 아주 조금 더 큰 값이 나옴.
"""

#극복
print((fnum * 10 + fnum2 * 10) / 10)

"""
참과 거짓의 변수는 is 또는 has 등 을 앞에 붙여주는게 좋음(부정문은 쓰지 않는다)
ex) is_empty = True O is_not_empty = False X
"""

# is_mz = True #True / False Boolean
# str = "python" #True
# str = "" #False
# list = [1, 2, 3] #True
# list = [] #False
# tuple = {} #False
# dict = {} #False
# num = 0 #False