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

# 왜 쓰느냐?
# 확장성 : 함수를 조합해서 비슷하지만 서로 다른 기능들을 확장

# 전략패턴 - 행동의 양상은 같은데, 행동의 디테일만 다른경우
# python에서는 고차함수로 함수의 조합을 통해 구현할 수 있음

def create_shopping_cart():
    """쇼핑카트를 생성하는 함수"""
    cart = {
        'items': [],
        'total_price': 0
    }
    return cart

def add_item(cart, item, price):
    """카트에 상품을 추가하는 함수"""
    cart['items'].append((item, price))
    cart['total_price'] += price

def checkout(cart, payment_strategy):
    """결제 전략을 주입받아서 결제 처리하는 함수"""
    return payment_strategy(cart['total_price'])

# 다양한 결제 전략들
def credit_card_payment(amount):
    print(f"신용카드로 {amount}원 결제")
    return {"method": "credit_card", "amount": amount, "fee": 0}

def mobile_payment(amount):
    print(f"모바일로 {amount}원 결제")
    discount = amount * 0.10  # 10% 할인
    final_amount = amount - discount
    print(f"모바일 할인: {discount}원")
    return {"method": "mobile", "amount": final_amount, "fee": 0}

def bank_transfer(amount):
    print(f"계좌이체로 {amount}원 결제")
    fee = 500  # 수수료
    final_amount = amount + fee
    print(f"이체 수수료: {fee}원")
    return {"method": "bank", "amount": final_amount, "fee": fee}

cart = create_shopping_cart()
add_item(cart, "노트북", 100000)
add_item(cart, "마우스", 20000)

# 실행 시점에 전략(결제 방법) 선택
print("=== 신용카드 결제 ===")
result1 = checkout(cart, credit_card_payment)

print("\n=== 모바일 결제 ===")
result2 = checkout(cart, mobile_payment)

print("\n=== 계좌이체 ===")
result3 = checkout(cart, bank_transfer)


################################################


# 사용자 입력 검증 시스템
def validate_input(user_input, validation_strategy):
    """사용자 입력을 검증하는 고차함수"""
    return validation_strategy(user_input)

# 검증 전략들
def password_validation(password):
    """비밀번호 검증: 8자 이상, 특수문자 포함"""
    if len(password) < 8:
        return {"valid": False, "message": "비밀번호는 8자 이상이어야 합니다"}
    if not any(char in "!@#$%^&*" for char in password):
        return {"valid": False, "message": "특수문자를 포함해야 합니다"}
    return {"valid": True, "message": "유효한 비밀번호입니다"}

def email_validation(email):
    """이메일 검증: @ 포함, .com 또는 .kr로 끝남"""
    if "@" not in email:
        return {"valid": False, "message": "이메일에 @가 없습니다"}
    if not (email.endswith(".com") or email.endswith(".kr")):
        return {"valid": False, "message": "이메일이 .com 또는 .kr로 끝나야 합니다"}
    return {"valid": True, "message": "유효한 이메일입니다"}

def phone_validation(phone):
    """전화번호 검증: 010으로 시작, 11자리 숫자"""
    # 하이픈 제거
    phone = phone.replace("-", "")
    if not phone.startswith("010"):
        return {"valid": False, "message": "010으로 시작해야 합니다"}
    if len(phone) != 11 or not phone.isdigit():
        return {"valid": False, "message": "11자리 숫자여야 합니다"}
    return {"valid": True, "message": "유효한 전화번호입니다"}

# 사용 예시
print("=== 비밀번호 검증 ===")
result1 = validate_input("1234", password_validation)
print(result1["message"])

result2 = validate_input("mypassword!@", password_validation)
print(result2["message"])

print("\n=== 이메일 검증 ===")
result3 = validate_input("testgmail.com", email_validation)
print(result3["message"])

result4 = validate_input("test@gmail.com", email_validation)
print(result4["message"])

print("\n=== 전화번호 검증 ===")
result5 = validate_input("010-1234-5678", phone_validation)
print(result5["message"])

