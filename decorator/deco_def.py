# --------------------------------------------
# 1 원래 함수
# --------------------------------------------
def greet(name):
    print(f"안녕하세요, {name}님!")


greet("철수")


# --------------------------------------------
# 2 데코레이터 정의 (args, kwargs 없이)
# --------------------------------------------
def add_log(func):
    # 내부에서 받을 인자가 정해져 있으므로 name만 명시
    def wrapper(name):
        print(f"[LOG] 함수 {func.__name__} 호출됨")
        result = func(name)  # 그대로 전달
        print(f"[LOG] 함수 {func.__name__} 종료됨")
        return result

    return wrapper


logged_greet = add_log(greet)  # @데코레이터 와 동일한 효과
logged_greet("영희")


# @ 문법을 사용하면, greet = add_log(greet) 와 동일하다.
@add_log
def greet2(name):
    print(f"반갑습니다, {name}님!")


# 이 시점에서 greet2는 이미 add_log(greet2)가 되어 있다.
greet2("민수")


# --------------------------------------------
# 1️⃣ 데코레이터 정의
# --------------------------------------------
def calc(func):
    def wrapper(a, b):
        print(f"계산 중: {func.__name__}({a}, {b})")
        result = func(a, b)
        print(f"결과: {result}")
        return result

    return wrapper


# --------------------------------------------
# 2️⃣ 실제 연산 함수들에 적용
# --------------------------------------------
@calc
def add(a, b):
    return a + b


@calc
def multi(a, b):
    return a * b


# --------------------------------------------
# 3️⃣ 사용 예시
# --------------------------------------------
add(3, 5)
multi(4, 6)


# --------------------------------------------
# 1️⃣ 입력값 검증용 데코레이터
# --------------------------------------------
def validate_name(func):
    def wrapper(name):
        if not isinstance(name, str):
            print("[ERROR] 이름은 문자열이어야 합니다.")
            return None
        if not name.strip():
            print("[ERROR] 이름이 비어 있습니다.")
            return None
        if any([ch.isdigit() for ch in name]):
            print("[ERROR] 이름에 숫자가 들어갈 수 없습니다.")
            return None
        return func(name)

    return wrapper


# --------------------------------------------
# 2️⃣ 인사 함수에 검증 데코레이터 적용
# --------------------------------------------
@validate_name
def greet(name):
    print(f"안녕하세요, {name}님!")


# --------------------------------------------
# 3️⃣ 사용 예시
# --------------------------------------------
greet("철수")  # ✅ 정상
greet("")  # ❌ 빈 문자열
greet(123)  # ❌ 타입 오류
greet("영희123")  # ❌ 숫자 포함
