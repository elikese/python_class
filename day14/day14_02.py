# raise: 예외를 의도적으로 생성하는 방법
try:
    raise ValueError("이값은 유효한 값이 아닙니다")  # 내가 직접 error 인스턴스를 생성
except ValueError as e:
    print(e)

# 나이를 입력하라
num = "-10"
age = int(num)
# if age < 0:
#     raise ValueError("나이는 음수 일 수 없습니다")


# 커스텀 예외 1
class NegativeAgeError(Exception):
    pass


try:
    user_input = input("나이를 입력하세요 >>")
    user_age = int(user_input)

    if user_age < 0:
        raise NegativeAgeError("나이는 음수가 될수 없습니다")

except ValueError as e:
    print("숫자를 입력하세요")
except NegativeAgeError as e:  # e : 해당 Error의 인스턴스
    print(e)  # Error인스턴스의 __str__이 호출


# 커스텀 예외 2
class NegativeScoreError(Exception):
    def __init__(self, score):
        self.message = f"점수는 음수 일 수 없습니다. 입력된 값:{score}"
        super().__init__(self.message)

    def __str__(self):
        return self.message


try:
    user_input = input("점수를 입력하세요 >>")
    score = int(user_input)

    if score < 0:
        raise NegativeScoreError(score)

except ValueError as e:
    print("숫자를 입력하세요")
except NegativeScoreError as e:  # e : 해당 Error의 인스턴스
    print(e)  # Error인스턴스의 __str__이 호출


# 실습) 비밀번호 길이 검증실패시, 커스텀 에러 생성
# 비밀번호 길이가 8자 미만일때 : ShortPasswordError
# 메세지 -> 비밀번호는 8자 이상이어야 합니다, 현재 비밀번호 길이:


class ShortPasswordError(Exception):
    def __init__(self, password):
        self.message = f"비밀번호는 8자 이상이어야 합니다. 현재 비밀번호 길이:{len(password)}"
        super().__init__(self.message)


password = input("비밀번호를 입력하세요 >>")

try:
    if len(password) < 8:
        raise ShortPasswordError(password)

except ShortPasswordError as e:
    print(e)

# 실습2) 이메일 주소 검증
# 사용자에게 이메일 주소를 입력받고, @가 없거나 .com이 포함되지 않으면 InvalidEmailError 예외를 발생시킴.
# in연산자 써서 @검사, 문자열의 endswith써서 .com으로 끝나는지 검사
# 검사 통과 x -> InvalidEmailError를 발생 -> except로 잡아서 에러메세지 출력
# 검사 통과 o -> 올바른 출력입니다: 이메일 주소 출력


class InvalidEmailError(Exception):
    def __init__(self, email):
        self.message = f"유효하지 않은 이메일 형식입니다: {email}"
        super().__init__(self.message)


email = input("이메일 주소를 입력하세요 >>")

try:
    if "@" not in email or not email.endswith(".com"):
        raise InvalidEmailError(email)
except InvalidEmailError as e:
    print(e)
else:
    print(f"올바른 이메일 입니다: {email}")

"""
오류를 의도적으로 일으키는 이유
하나라도 실패하면 전체를 취소해야 하는 작업
명시적으로 예외를 발생시키는 게 올바른 방식

복잡한 로직에서 중단 시점을 통제하기 위해
여러 단계를 거쳐 처리하는 데이터 가공시, 
어느 한 조건이 안 맞으면 나머지를 안 해야 함.
"""
