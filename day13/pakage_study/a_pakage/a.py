# 이 파일을 직접 실행했을때만
# if문 코드블럭을 실행하라

# __name__
# 우리가 py파일을 실행시킨다.
# 그때 파이썬은 내부적으로 __name__ 이라는 변수를 만들어서 py파일들을 관리
# 내가 직접 실행시킨 py파일은 __name__ = "__main__" 으로 지정된다.
# 모듈은 __name__ = "모듈이름"(현재 이 모듈이 import된다면 "a_pakage.a")

print(__name__)


def add(num1, num2):
    return num1 + num2


class Calculation:
    def sub(self, num1, num2):
        return num1 - num2


if __name__ == "__main__":
    print("a에서 출력!")

# if __name__ == "__main__":
# 직접 이 py파일을 실행시킬때만 실행하고,
# import될땐 무시되는 코드
