# 함수 : 반복되는 작업을 이름 붙여 저장해 놓은 것
# 참고) 함수형 프로그래밍(Functional Programing) - 2015년부터 재유행
# 2010 ~ 코로나 직전까지 트렌드 : 스마트폰(개인마다 하나의 휴대용 pc가 생긴것)
# 필연적으로 웹서비스(페이스북, 인스타그램, 넷플릭스....)가 가장 돈을 잘 버는 블루오션
# 그당시 웹에서 가장 해결하기 힘든 문제 : 비동기, 동시성 처리 (기존의 스타일:OOP에서는 바뀌는 값에 대한 제한이 필요 -> 복잡성 증가)
# f(x) 함수라는것은 입력되는 순간 출력으로 결정되게 설계가 가능. -> 이 성질을 이용하면 바뀌는 값에 대해 신경을 꺼도 된다.
# 함수형 프로그래밍이 각광받는 기술로 다시 주목받는다. python / Javascript(Java 아님) 인도네시아(인도 아님) / kotlin
# 중요한건 어떻게 하면, 입력되는 순간 출력으로 결정되게 설계하느냐?(순수함수, 고차함수, 일급객체...)
# 지금은? OOP(클래스기반) + FP(함수기반) 합친 멀티패러다임 프로그래밍시대


# 매개변수 X 리턴 X
def greet():
    print("안녕하세요!")


greet()


# 매개변수 O, 리턴 X
# 매개변수(parameter) vs 일반변수
# 매개변수 -> 함수가 호출될때 외부에서 전달받는값을 저장하는 변수(함수 내부에서만 사용)
# 일반변수 -> 함수 내부 혹은 외부에서 "="로 대입해서 만든 변수
# 범위(scope) -> 변수를 사용할 수 있는 범위(영역)


def greet_person(name):  # name은 매개변수
    print(f"{name}님, 반갑습니다!")


# print(name) # name의 범위(scope)는 greet_person이라는 함수내로 한정
greet_person("홍길동")


# 매개변수 X, 리턴 O
def bark():
    return "멍멍"


bark_sound = bark()
print(bark_sound)


# 매개변수 O, 리턴 O
def add(x, y):
    return x + y


result = add(3, 5)
print(result)

# 실습) 숫자가 짝수인지 홀수인지 알려주는 함수
# 함수이름은 check_even
# 매개변수로 숫자를 받음
# bool자료형(True or False)을 리턴 - 짝수(True) / 홀수(False)


def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# 매개변수에 기본값설정이 가능하다.
# 함수 호출시, 해당 매개변수 인자를 생략해도 기본값이 사용되도록 만들 수 있다.
# print문도 기본값 설정이 되어있다. end='\n' 개행이 기본값이고, sep=' '한칸 띄운게 기본값이다.
def greet(name="친구"):
    print(f"안녕, {name}!")


greet()
greet("친구야")

# 함수 매개변수 기본값 설정시 주의사항 : 기본값이 없는 매개변수가 뒤에 오면 안된다
# 함수호출시 순서를 기준으로 변수에 할당하기 때문에
# 기본값설정이 되어있는게 나중 순서로 와야 호출 시 명확하게 변수에 할당할 수 있다.
# def greet2(name="친구", age):  # 에러
#     print(age, name)
# 호출시 age가 20이라고 생각하고 greet2(20) 호출하면, 컴퓨터는 이 20을 name이라고 생각하게 된다.
# 그럼 기본값을 설정한 이유가 없다 -> 이런 모호함을 없애기 위해서 에러를 발생하게 설계


# isdecimal
# 문제 -> 소수, 음수 구분이 x
# 소수, 음수 구분없이 숫자인지 검사하는 함수를 만들어보고 싶다!
def is_number(s):
    s.strip()  # 혹시나 있을 공백제거

    # 부호 처리
    # if s.startswith("-") or s.startswith("+"):
    if s.startswith(("-", "+")):
        s = s[1:]

    # 소수점 처리
    # 1. "."이 1개 혹은 0개여야 한다
    if s.count(".") > 1:
        return False

    # 2. "." 앞뒤로 0~9의 정수가 있어야한다 ex) ".5" "3."
    if "." in s:
        left, right = s.split(".")

        if not left or not right:  # "."만 있는 경우, ".5" or "3."
            return False

        if left and not left.isdecimal():  # "a_pakage.3"
            return False

        if right and not right.isdecimal():  # "3.a_pakage"
            return False

        return True

    return s.isdecimal()


# 테스트
print(is_number("3.14"))
print(is_number("-3.14"))
print(is_number(".1"))
print(is_number("3.r"))
print(is_number("a_pakage.3"))
