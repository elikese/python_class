class Greeter:
    def __init__(self, name):
        self.name = name

    # 함수처럼 동작하는 객체
    def __call__(self, time):
        print(f"좋은{time}입니다, {self.name}님!")


# 객체 생성
greet = Greeter("홍길동")

# ✅ 객체를 함수처럼 호출할 수 있음
# 실제로는 greet.__call__("아침") 호출
greet("아침")


class Logger:
    def __init__(self, func):
        self.func = func  # 감쌀 함수 저장

    def __call__(self, a, b):
        print(f"[LOG] {self.func.__name__} 호출됨: ({a}, {b})")
        result = self.func(a, b)
        print(f"[LOG] {self.func.__name__} 결과: {result}")
        return result


# add = Logger(add) 동작 -> 생성자를 호출함 -> 객체가 됨
# -> add는 Logger로 부터 만들어진 객체
@Logger
def add(a, b):
    return a + b


@Logger
def multi(a, b):
    return a * b


# __call__(3,5)가 호출됨
add(3, 5)

# __call__(2,4)가 호출됨
multi(2, 4)


class Power:
    def __init__(self, n):
        self.n = n  # ✅ 숫자 속성 (ex: 제곱 지수)

    def __call__(self, func):
        # 이 객체 자체가 데코레이터로 작동
        def wrapper(x):
            result = func(x)
            powered = result**self.n  # 숫자 속성을 이용
            print(f"{result} ** {self.n} = {powered}")
            return powered

        return wrapper


@Power(2)
def double(x):
    return x * 2


@Power(3)
def triple(x):
    return x * 3


print(double(3))  # (3*2)^2 = 36
print(triple(2))  # (2*3)^3 = 216


# 자주쓰는 객체들은 미리 정의해 둘 수 있음.
class MathTools:
    # 클래스 변수에 담겨 있는 객체들
    square = Power(2)
    cube = Power(3)
    quad = Power(4)


@MathTools.square
def half(x):
    return x / 2


@MathTools.cube
def add_ten(x):
    return x + 10


half(4)
add_ten(2)
