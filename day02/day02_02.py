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

# 묵시적 형변환(자동으로 알아서 눈치껏 형변환해주는 것)
# int + float => float , 나누기하면 자동으로 결과는 float으로 형변환
# 참고) bool + int => int(True => 1 / False => 0)
# if 뒤에 문자열 / 숫자 묵시적으로 논리값으로 형변환 => "" / 0 False로 자동 형변환. "어쩌고" / 100 True로 자동 형변환.\

# 실습2) 할인계산기
# 상품 가격을 input()을 통해 입력받고,
# 10만원 이상이면 10%할인. 아니면 할인없음. 최종 결제 금액을 print하시오.
# input()으로 받은 데이터의 자료형은 str입니다!!!!
price = int(input("상품 가격을 입력하세요: "))
discounted_price = price * 0.9
final_price = discounted_price if price >= 100000 else price
print(final_price)
