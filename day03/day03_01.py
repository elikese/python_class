# 제어문 (조건문 + 반복문)

# 조건문 (python엔 switch문 없음)
# if(bool자료형):
#   true일때 코드실행블럭 (들여쓰기 주의)
# elif(bool자료형):
#   true일때 코드실행블럭 (들여쓰기 주의)
# else:
#   그 외의 조건일때(=위의 조건들과 맞지 않을 때) 코드실행 블럭

# 들여쓸때는 tab키 사용권장! 일반적으로 1tab = 4space-bar
# 파이썬은 들여쓴 코드블럭을 하나의 경계로 인식한다.

if True:
    print("참입니다")
if False:
    print("들여쓴 코드")
print("if와 상관없이 실행되는 코드")

# 실습) 할인계산기
# 상품 가격을 input()을 통해 입력받고,
# 10만원 이상이면 10%할인. 아니면 할인없음. 최종 결제 금액을 print하시오.
# input()으로 받은 데이터의 자료형은 str입니다!!!!
price = "110000"
int_price = int(price)
discount_price = int_price * 0.9
if int_price >= 100000:
    print(discount_price)
else:
    print(int_price)

# if (bool자료형) bool자료형은 논리연산의 결과 or 조건연산의 결과가 일반적.
# if ~ elif ~ else : 순차적으로 검사(위 -> 아래), 조건이 맞으면 해당 코드 블럭을 실행하고 탈출.

# 묵시적 형변환(자동으로 알아서 눈치껏 형변환해주는 것)
# int + float => float , 나누기하면 자동으로 결과는 float으로 형변환
# 참고) bool + int => int(True -> 1 / False -> 0)
# if/elif 뒤에 문자열 / 숫자는 묵시적으로 논리값(bool형)으로 형변환된다 ("" / 0) -> False로 자동 형변환. ("어쩌고" / 100) -> True로 자동 형변환.

# 조건이 정량적일때(숫자)
age = 10
if age >= 20:
    print("성인")
elif age >= 17:
    print("고등학생")
elif age >= 14:
    print("중학생")
elif age >= 8:
    print("초등학생")
else:
    print("미취학아동")

# 조건이 논리적일 때
# 특정 조건 코드 블럭이 실행된다는건, 이전 조건이 False라는 것

is_submitted = True
is_late = True
is_cheated = False

# 당연히 if문은 중첩이 됩니다.

if is_submitted:
    print("제출")
    if is_cheated:
        print("부정행위")
    elif is_late:
        print("지각 제출")
else:
    print("미제출")

# 논리적으로 오류가 없으면, 정답은 없습니다. -> 가독성, 코드관리의 측면에서 고민할 단계

# 실습) bmi 계산기
# bmi = 체중(kg) / 신장(m)*신장(m)
# 18.5 미만 -> 저체중 / 18.5 이상 25 미만 -> 정상 / 25 이상 30미만 -> 과체중 / 30 이상 비만
# input을 통해 체중과 신장을 입력받아, bmi를 계산하여,해당하는 상태를 출력하시오

weight = float(input("체중을 입력하세요(kg):"))
height = float(input("신장을 입력하세요(cm):")) // 100
bmi = weight / (height**2)

# bmi는 소숫점 2째리에서 반올림하셔야 합니다. round() 사용!
rounded_bmi = round(bmi, 2)

if bmi >= 30:
    print("비만")
elif bmi >= 25:
    print("과체중")
elif bmi >= 18.5:
    print("정상")
else:
    print("저체중")
