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

# 조건연산자(삼항 연산자)
# if 뒤에 조건식을 써도 되지만, 최종적으로는 bool자료형이 오기만 하면 된다.
score = 80
isPass = score >= 60
result = "pass" if isPass else "fail"
print(result)

result = ""
if isPass:
    result = "pass"
else:
    result = "fail"
print(result)

# 여러개 조건
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(grade)

result = ""
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
else:
    result = "C"
print(result)

# 실습1) 로그인 조건확인
# real_id = "python" real_pw = "1234"이다.
# input()을 통해 id와 pw를 입력받고, 입력받은 id와 pw가 real_id / real_pw와 같은지 검사하여
# 로그인성공여부(성공하면, "로그인성공") (실패하면, "로그인실패")를 print 하시오.
real_id = "python"
real_pw = "1234"
input_id = input("아이디 입력: ")
input_pw = input("비밀번호 입력: ")

isLogin = real_id == input_id and real_pw == input_pw
# 로그인성공 ? isLogin => true / 실패 ? isLogin => false
print("로그인성공" if isLogin else "로그인실패")
