# 함수 복습
# def minor_filter(**civil):
#     if civil["age"] < 20:
#         print(f"미성년자! {civil}")
#
# for civil in civil_list:
#     minor_filter(**civil)

# 코드는 위에서 아래로 순차 실행된다는 기본 원칙이 있는데,
# 함수호출 과정에서 코드가 위로 다시 올라가는게 헷갈릴 수 있음
# 함수 정의 / 함수 호출
# 함수 정의 : 함수는 특정 작업(코드)을 실행하지 않고, 이렇게 실행할 거라고 미리 작성해 둔 것
# 실행시점? 함수 호출이 될때
# fn: 함수이름(함수를 저장한 변수), fn(): 함수를 호출해서 실행시킨 것

# 일반변수도 위에서 우리가 미리 만들고 밑에서 재사용 함
x = 10
y = x + 10

# 함수도 동일하게 미리 만들고 밑에서 재사용 함
# 함수는 코드블럭을 담는 변수


# 고차함수/콜백함수
# 고차함수 : 함수를 매개인자로 전달 "받는" 함수 : 외부에서 함수를 주입받게끔 설계
# 콜백함수 : 매개인자로 전달 "되는" 함수 : 함수가 주입되게끔 설계
# 콜백함수는 함수를 사용하는 사람이 호출하지 않고, 고차함수에 의해 호출 된다.


def calculation(num1, num2, fx):  # fx가 매개인자로 전달된다.
    return fx(num1, num2)


def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiple(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


plus_result = calculation(10, 5, plus)
minus_result = calculation(10, 5, minus)
multiple_result = calculation(10, 5, multiple)
divide_result = calculation(10, 5, divide)

print(plus_result)
print(minus_result)
print(multiple_result)
print(divide_result)

# 이걸 도대체 왜 쓰느냐?
# 확장 : 함수를 조합해서 비슷하지만 서로 다른 기능들을 확장
# 전략패턴 - 행동의 양상은 같은데, 행동의 디테일만 다른경우
# python에서는 고차함수로 함수의 조합을 통해 구현할 수 있음

# 문서 출력하고, 처리 끝나면 알려주세요(알려주는 방법이 여러개)


def print_document(fx):
    print("---------")
    print("문서를 출력합니다")  # 문서 출력
    print("출력완료!")
    fx()  # 알려주는 방법만 다르고 나머지 흐름이 동일
    print("정리시작")
    print("정리완료")
    print("---------")


def notify_by_email():
    print("이메일 전송")


def notify_by_sms():
    print("문자 전송")


def notify_by_kakao():
    print("카카오톡 전송")


print_document(notify_by_email)
print_document(notify_by_sms)
print_document(notify_by_kakao)


# 배달앱(결제)
def delivery_order(payment_function):
    # 주문 한 음식들 total_price 계산
    # 계산결과 15000원이 나옴
    total_price = 15000
    payment_function(total_price)


def credit_card(price):
    print("카드로 결제!")
    # PG회사랑 연동되는 코드
    return price


def kakao_payment(price):
    print("카카오로 결제!")
    return price


# naver결제 : naver_payment
# 이벤트: 15000원 이상 주문시, 1000원 할인
def naver_payment(price):
    print("네이버로 결제!")
    return price - 1000


# 장점 - 새로운 payment방법이 생겨나도, delivery_order를 바꾸지 않아도 된다.
# 각 payment에 맞춰서 디테일을 바꿔 줄 수 있다.
# 새로운 payment가 생기면 그 payment에 대한 함수만 만들어서 넘기면 된다.
