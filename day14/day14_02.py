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
        self.message = (
            f"비밀번호는 8자 이상이어야 합니다. 현재 비밀번호 길이:{len(password)}"
        )
        super().__init__(self.message)

    def __str__(self):
        return self.message


password = input("비밀번호를 입력하세요 >>")

try:
    if len(password) < 8:
        raise ShortPasswordError(password)

except ShortPasswordError as e:
    print(e)
