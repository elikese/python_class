# 함수의 스코프(범위)


# 1. 함수안에서 선언된 변수는 함수안에서만 살아있다
def greet():
    name = "Alice"
    print(name)


greet()
print(name)


print("----------------------")
# 2. 함수 안에서 전역변수 읽기만 할 때는 상관없음
x = 10


def print_x():
    print(x)  # ✅ 10


print_x()

print("----------------------")
# 3. 함수 안에서 전역변수 수정할 때는 global 필요
x = 10


def change_x():
    x += 1


change_x()


def change_x():
    global x  # global을 하면 수정이 가능
    x += 1
