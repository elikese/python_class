# *args 패킹 -> 여러값을 하나의 tuple로 묶어서 전달
# **kwargs 패킹 -> 여러값을 하나의 dict로 묶어서 전달
import random


def make_user(username, **details):
    user = {"name": username}
    user.update(details)
    return user


user1 = make_user("홍길동", age=20, 거주지="부산")
print(user1)
user2 = make_user("홍길동", age=20, 거주지="부산", name="박길동")
print(user2)

# **kwarg 언패킹 가능!


def print_user(**kwargs):
    print(kwargs)


# print_user(user1)  # 'key=value' 형태가 아니라서 에러
print_user(**user1)  # 이미 dict로 패킹되어있다고 알려주는것


# 나이 검사
def make_civil(name="", age=0):
    civil = {"name": name, "age": age}
    return civil  # dict


l_names = ["김", "박", "이"]
f_names = ["철수", "영희", "병철", "국진"]
civil_list = []
for l_name in l_names:
    for f_name in f_names:
        full_name = l_name + f_name
        age = random.randint(8, 50)
        civil_list.append(make_civil(full_name, age))

print(civil_list)


def minor_filter(**civil):
    if civil["age"] < 20:
        print(f"미성년자! {civil}")


for civil in civil_list:
    minor_filter(**civil)

# 인자로 전닫되는 함수(콜백함수) - *참고) 일급객체(first object): 함수는 값이다.
# 가장 헷갈리는것
# fn 함수 그 자체, fn(): 함수를 호출해서 실행시킨 결과


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
# 공통의 흐름이 있는데, 딱 한부분만 좀 다르다? 이럴 때

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

import time

time.sleep(0)  # 지정한 초만큼 일시중지
print(time.time())  # 1970-01-01 00:00:00초 기준으로 현재까지 몇초가 흘렀나


# 함수의 실행 속도 (같은 결과를 보이지만, 빠른게 뭔지 궁금할때)
def perf_timer(fx):
    print("타이머 시작")
    start_time = time.time()
    fx()
    end_time = time.time()
    print("타이머 종료")
    print(f"걸린시간 : {end_time - start_time}")


perf_timer()
