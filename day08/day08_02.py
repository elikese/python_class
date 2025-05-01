# *args 패킹
# 여러개로 들어온 매개변수들을 tuple에 담아서 하나로 만들어 준다.
# 매개변수의 갯수가 가변적일때(변할때) 사용 된다.
def args_function(*args):  # 매개변수명은 자유(매개변수 앞에 *이 하나 있냐 없냐)
    print(type(args))
    for index, value in enumerate(args):
        print(f"{index}번째 과일: {value}")


args_function("사과", "바나나", "포도")


# 실습) 매개변수로 들어오는 모든 숫자들을 더하고, 더한값을 리턴하는 함수를 만들어주세요
def num_sum(*args):
    arg_sum = 0  # arg_sum의 범위(스코프) : 함수안에서만 사용가능
    for num in args:
        arg_sum += num
    return arg_sum


print(num_sum(10, 20, 30))


# order_pizza라는 함수를 정의. 매개변수로는 *args를 통해 여러가지 토핑을 받는다.
# 함수 내부에는 pizza라는 dict가 있습니다. 기본값 9900원, 토핑에 따라 추가 금액발생
# 함수는 최종적으로 피자에 담긴 토핑에 따라 계산을 해서 최종가격을 리턴합니다.

toppings = {
    "페퍼로니": 500,
    "치즈": 300,
    "올리브": 250,
    "소세지": 800,
    "파인애플": 1500,
}


def order_pizza(*args):
    pizza = {"plain": 9900, "topping": 0}
    # 1. args로 받은 토핑리스트들의 각 가격을 합친다.(price_sum 변수로 누적합)
    # 2. pizza[topping]의 value를 업데이트 해준다.
    # 3. 최종 pizza의 value들의 합(총 가격)을 리턴한다.
    price_sum = 0
    for topping in args:
        price_sum += toppings[topping]

    pizza["topping"] = price_sum
    pizza.update({"topping": price_sum})

    total_price = 0
    for price in pizza.values():
        total_price += price

    return total_price


print(order_pizza("페퍼로니", "올리브"))

# 문제가 발생!
# 함수를 호출할때, 우리가 기존에 있는 토핑만 주문가능
# 그 외의 토핑을 입력했을 때를 검증하는 로직이 빠진 것


# 토핑을 검증하는 함수를 만들어봅시다
def is_our_toppings(*args):

    for topping in args:
        if topping not in toppings.keys():
            print(f"{topping}은 제공하지 않습니다")
            print(f"토핑메뉴 : {toppings}")
            return False
    return True


print("--------")
if is_our_toppings("페퍼로니", "올리브", "소세지"):
    print(order_pizza("페퍼로니", "올리브", "소세지"))

# 추가로 확장 -> 메뉴를 직접 타이핑 쳐서 입력하는걸 변경(숫자로 변경)


# *args주의사항) 키워드 전용 매개변수(*arg)
def greetings(name, *messages, finish="!!"):
    print(f"안녕하세요, {name}씨")
    for messages in messages:
        print(messages, end="")
    print(finish)


# *args는 가변매개변수 -> 몇개가 들어올지 예상할 수 없다
# *args의 순번 이후에 오는 매개변수는 함수 호출시 명시적으로 작성해줘야 합니다.
greetings("홍길동", "반갑", "습니다", "~!")
greetings(
    "홍길동", "반갑", "습니다", finish="~!"
)  # 매개변수의 이름을 정확히 기입해서 알려줘야한다.

# *args 언패킹! -> 순서로 관리되는 것들을


def print_family_name(mother, father, *siblings):
    print(f"어머니 : {mother}")
    print(f"아버지 : {father}")
    for index, sibling in enumerate(siblings):
        print(f"형제{index + 1} : {sibling}")


print_family_name("김영희", "박길동", "박첫쨰", "박둘째", "박셋째")

# 매개변수에 패킹으로 가능한 자료형 -> 리스트, 튜플, 리스트비슷한것들, set(순서없음)...iterable한것 모두 다
# dict도 가능은 하지만, *dict하게되면, key만 튜플로 묶어서 가져갑니다.
sibling_list = ("박첫째", "박둘째", "박셋째")

print_family_name(
    "김영희", "박길동", *sibling_list
)  # *을 붙히면, 이미 패킹되어 있구나라는걸 인식해준다.

# 그 이후에 추가해주면 같이 패킹해줍니다.
print_family_name("김영희", "박길동", *sibling_list, "박넷째")
