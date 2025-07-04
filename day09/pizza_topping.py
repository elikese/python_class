# 피자 주문 시스템
# *args 복습
# 기본피자 + topping들 추가(여러개를 가변적으로)


# 토핑 메뉴 정의
topping_menu = {
    "페퍼로니": 500,
    "치즈": 300,
    "올리브": 250,
    "소세지": 800,
    "파인애플": 1500,
}

BASE_PRICE = 9900  # 기본 피자 가격

def validate_toppings(*toppings):
    """토핑이 메뉴에 있는지 검증하는 함수"""
    for topping in toppings:
        if topping not in topping_menu:
            print(f"{topping}은 제공하지 않는 토핑입니다")
            print(f"🍕 사용 가능한 토핑: {list(topping_menu.keys())}")
            return False
    return True

def calculate_topping_price(*toppings):
    """토핑들의 총 가격을 계산하는 함수"""
    price_sum = 0
    for topping in toppings:
        price_sum += topping_menu[topping]
    return price_sum

def order_pizza(*toppings):
    """피자를 주문하는 함수"""
    # 토핑 검증
    if not validate_toppings(*toppings):
        return None

    # 토핑 가격 계산
    topping_price = calculate_topping_price(*toppings)

    # 총 가격 계산
    total_price = BASE_PRICE + topping_price

    # 주문 내역 출력
    print(f"주문 내역:")
    print(f"기본 피자: {BASE_PRICE}원")
    if toppings:
        print(f"토핑: {toppings} (+{topping_price}원)")
    print(f"총 가격: {total_price}원")

    return total_price

# 테스트
print("=== 정상 주문 ===")
order_pizza("페퍼로니", "올리브")

print("\n=== 잘못된 토핑 주문 ===")
order_pizza("페퍼로니", "버섯", "올리브")

print("\n=== 토핑 없는 주문 ===")
order_pizza()