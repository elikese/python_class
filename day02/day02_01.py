# 형변환 : 자료형 바꾸기
# int(): 정수로 바꿔준다
print(int(11.0))  # 11
print(int("11"))  # 11

# float(): 실수로 바꿔준다
print(float(11))
print(float("11"))

# str(): 문자열로 바꿔준다
print(str(100) + "원")

# bool(): 논리값으로 바꿔준다 (True or False)
print(bool(""))
# str = "" #False str = "어쩌고" #True
# num = 0 #False num = 100 #True
# list, dict, tuple 내부가 비어있으면 False

# 연산자

# 산술 연산자
# number (결과값의 자료형 : number)
print(20 + 20)
print(20 - 20)
print(20 * 20)
print(20 / 10)
print(20 // 8)  # 몫
print(20 % 8)  # 나머지
print(2**2)  # 2의 2승

# 어느 게시판에서는 한 페이지당 20개의 게시글이 보여진다.
# 게시판의 총 게시글은 162개이다.
# 게시판의 총 페이지의 갯수와 마지막페이지의 게시글 수를 print 하시오.
total_post = 162
total_page = 162 // 20
last_page_post = 162 % 20
print(f"총페이지:{total_page}, 마지막 페이지 게시글 수:{last_page_post}")

# str (결과값의 자료형 : str)
print("안녕" + "하세요")
print("안녕하세요 " * 3)

# 대입연산자 (결과값의 자료형 : 대입한 자료형)
x = 10
x += 1  # x = x + 1
x -= 1  # x = x - 1
x *= 2  # x = x * 2
x /= 2  # x = x / 2

# 비교연산자 (결과값의 자료형 : bool)
x = 10
y = 20
z = 10
print(x == z)  # True
print(x < y)  # True
print(x > y)  # False
print(x == y)  # False
print(x != y)  # True
print(x <= y)  # True
print(x >= z)  # True

print("------------")
# 논리 연산자 (결과값의 자료형 : bool)
# not/ and/ or
a = True
b = False
print(not a and b)  # False
print(a or b)  # True
print(not a)  # False

print(x == z)
print(not x == z)
print(not x == z and x == z)
print(not x == z or x == z)

# 연산자 우선순위
# ( ) > ** > *, /, //, % > +, - > 비교연산자(==, !=, >, <) > not(논리연산자) > and(논리연산자) > or(논리연산자)
a = True or False and False
print(f"a의결과: {a}")
a = (True or False) and False
print(f"a의결과: {a}")
a = (True or False) and not False
print(f"a의결과: {a}")
