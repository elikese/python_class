# 조건연산자(삼항 연산자)
score = 80
isPass = score >= 60
result = "pass" if isPass else "fail"
print(result)

# 여러개 조건
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(grade)

# 실습1) 로그인 조건확인
# real_id = "python" real_pw = "1234"이다.
# input()을 통해 id와 pw를 입력받고, 입력받은 id와 pw가 real_id / real_pw와 같은지 검사하여
# 로그인성공여부(성공하면, "로그인성공") (실패하면, "로그인실패")를 print 하시오.
real_id = "python"
real_pw = "1234"
input_id = input("아이디 입력: ")
input_pw = input("비밀번호 입력: ")

isLogin = (input_id == real_id) and (input_pw == real_pw)
# 로그인성공 ? isLogin => true / 실패 ? isLogin => false
print("로그인성공" if isLogin else "로그인실패")

# 실습2) 할인계산기
# 상품 가격을 input()을 통해 입력받고,
# 10만원 이상이면 10%할인. 아니면 할인없음. 최종 결제 금액을 print하시오.
# input()으로 받은 데이터의 자료형은 str입니다!!!!
price = int(input("상품 가격을 입력하세요: "))
discounted_price = price * 0.9
final_price = discounted_price if price >= 100000 else price
print(final_price)
