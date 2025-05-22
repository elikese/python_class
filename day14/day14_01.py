# 예외: 예상하지 못한 ERROR
# 예외도 클래스
# 에러가나면 예외클래스의 객체(인스턴스)가 생성된다
# 예외 클래스의 인스턴스가 생성되면, 파이썬이 콘솔에 에러메세지를 출력해준다

# 예외 처리 문법
"""
try:
    예외가 날 수 있는 코드
except (예외종류1, 예외종류2...):
    예외 발생 시 실행할 코드
"""

# 빨간줄 : SyntaxError

# 파이썬은 한줄한줄 코드를 해석한다(인터프리터)
# 예외가 발생하면, Error 인스턴스를 생성
# Error인스턴스가 생성되면 인터프리터는 해석을 멈추고, 에러메세지를 콘솔에 출력

# try 블록이 시작되면
# Error인스턴스가 생성되면, 예외를 처리해줄 except구문을 찾습니다
# 찾으면, 그 블록으로 다시 진행
# 못찾으면 해석을 멈추고, 에러메세지를 콘솔에 출력

# print(1)
# print(2 / 0)  # 여기서 error발생! -> 코드해석 멈춤
# print(3)


# 예외 종류
# 1. SyntaxError: 문법에러 (코드 아래에 빨간 줄)
# 2. TypeError: 타입이 맞지 않은 '연산'시 발생
try:
    a = "hello"
    b = 3
    print(a + b)  # TypeError: 문자열 + 숫자 -> 타입이 맞지않는 연산
except TypeError as e:  # as e => TypeError 의 인스턴스를 e라는 변수에 담음
    print("TypeError 발생!")
    print("에러내용:", e)  # __str__() 이 호출된 것, e는 에러로그 남기는 용

# 3. NameError: 선언되지 않은 변수 사용 시 발생
try:
    print(x)
    x = 3
except NameError as e:
    print("NameError 발생!")
    print(e)

# 4. IndexError: 인덱스 범위를 벗어났을때
try:
    list = [1, 2, 3]
    print(list[100])  # 범위초과
except IndexError as e:
    print("IndexError 발생!")
    print(e)

# 5. KeyError: dict에 없는 키를 접근할 때
try:
    dict_data = {"name": "홍길동", "age": 20}
    print(dict_data["gender"])
except KeyError as e:
    print("KeyError 발생!")
    print(e)

# 6. ValueError: 타입은 맞는데, 값이 부적절한 경우
try:
    a = "abc"
    int(a)
    # int()는 문자열 받을 수 있음, 근데 그 값이 숫자처럼 생긴 문자열이어야 됨
except ValueError as e:
    print("ValueError 발생!")
    print(e)

try:
    names = ["철수", "영희"]
    names.remove("병철")
    # remove()는 물자열 받을 수 있음, 근데 그 값이 리스트에 있는 값이어야 됨.
except ValueError as e:
    print("ValueError 발생!")
    print(e)

# 7. ImportError: 존재하지 않는 모듈을 import할 때
# 8. IndentationError: 들여쓰기 잘 못 했을 때
# 9. ZeroDivisionError: 0으로 나누려고 할 떄

# try:
#     num = input("숫자를 입력하세요 >>")  # 에러 가능성 : x
#     int_num = int(num)  # 에러 가능성 : ValueError
#     print(10 / num)  # 에러 가능성: ZeroDivisionError
# except:
#     # 모든 예외를 처리할 수 있음(권장 x)
#     print("에러발생!")

# try:
#     num = input("숫자를 입력하세요 >>")  # 에러 가능성 : x
#     int_num = int(num)  # 에러 가능성 : ValueError
#     print(10 / num)  # 에러 가능성: ZeroDivisionError
# except (ValueError, TypeError) as e:
#     print("0을 제외한 숫자를 입력하세요")
#     print("에러로그:", e)

try:
    num = input("숫자를 입력하세요 >>")  # 에러 가능성 : x
    int_num = int(num)  # 에러 가능성 : ValueError
    print(10 / int_num)  # 에러 가능성: ZeroDivisionError
except ValueError as e:
    print("숫자를 입력하세요.")
    print("에러로그:", e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print("에러로그:", e)
