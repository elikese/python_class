# 반복되는 코드를 하나의 "이름"으로 지정해두는 것
# 나중에 필요할 때마다 호출해서 재사용할 수 있음.
# 변수는 값을 저장 / 함수는 코드를 저장

"""
함수 정의
def 함수이름(매개변수1, 매개변수2...):
    코드

    return 값

함수 사용(호출)
함수이름()
"""


# 매개변수 X 리턴 X


# 함수 정의
def greeting():
    print("안녕하세요!")


# 함수 사용(호출) -> 함수가 가지고 있던 코드가 실제 실행 됨
greeting()


# 매개변수 O, 리턴 X
# 매개변수(parameter) vs 일반변수
# 매개변수 -> 함수가 호출될때 외부에서 전달받는값을 저장하는 변수(함수 내부에서만 사용)
# 일반변수 -> 함수 내부 혹은 외부에서 "="로 대입해서 만든 변수
# 범위(scope) -> 변수를 사용할 수 있는 범위(영역)


def greet_person(name):  # name은 매개 "변수": 함수안에서만 유효한 변수
    print(f"{name}님, 반갑습니다!")


# "홍길동" 값이 함수로 전달되어서
# 함수는 name이라는 매개변수에 "홍길동"이라는 값을 저장 함.
greet_person("홍길동")

name1 = "홍길동"
name2 = name1
print(f"name2: {name2}")

# name2가 저장한 값이 함수로 전달되어서
# 함수는 name이라는 매개변수에 name2가 저장하고 있던 값을 저장 함.
greet_person(name2)


# 매개변수 X, 리턴 O
def bark():
    return "멍멍"


bark_sound = bark()
print(bark_sound)
print(bark())  # 리턴이 있으면 함수 호출 결과가 값이 된다.


# 매개변수 O, 리턴 O
def add(x, y):
    return x + y


result = add(3, 5)
print(result)
print(f"add(1,2) 호출 결과: {add(1, 2)}")
add(add(1, 2), 3)  # 리턴이 있으면 값이 되니까 값으로서 바로 사용이 가능


# 주민등록번호 처리
# 9911221234567


# 유효한 주민등록 번호인지 검사
# 1. 총 13자리 인지 검사
# 2. 숫자로 이루어진게 맞는지 검사
# 3. 01~12월 / 01~31일 검사
# 4. 뒷자리 1~4 성별 검사
def is_valid_pn(pn):
    # 하이픈 제거
    pn = pn.replace("-", "")

    # 13자리 검사
    if not len(pn) == 13:
        return False

    # 숫자인지 검사
    if not pn.isdecimal():
        return False

    # 월 검사
    if int(pn[2:4]) < 1 or int(pn[2:4]) > 12:
        return False

    # 일 검사
    if int(pn[4:6]) < 1 or int(pn[4:6]) > 31:
        return False

    # 성별 숫자 검사
    if int(pn[6]) < 1 or int(pn[6]) > 4:
        return False

    return True


result = is_valid_pn("910103-3122923")
print(f"결과: {result}")

# 실습) 주민번호를 매개변수로 받아서
# 주민번호 뒷자리를 분석하여 남자인지 여자인지 판단하는 함수를 만들어 주세요
# 남자면 문자열 "남자"를 리턴. 여자면 문자열 "여자"를 리턴.
# 함수이름: get_gender


def get_gender(pn):
    if not is_valid_pn(pn):
        return "유효하지 않은 주민등록번호입니다."

    gender_digit = int(pn[7])

    if gender_digit in [1, 3]:
        return "남자"
    elif gender_digit in [2, 4]:
        return "여자"


print(get_gender("010103-3122923"))


# 매개변수에 기본값설정이 가능하다.
# 함수 호출시, 해당 매개변수 인자를 생략해도 기본값이 사용되도록 만들 수 있다.
# print문도 기본값 설정이 되어있다. end='\n' 개행이 기본값이고, sep=' '한칸 띄운게 기본값이다.
def greet(name="홍길동"):
    print(f"안녕, {name}!")


greet()
greet("김길동")

# 함수 매개변수 기본값 설정시 주의사항 : 기본값이 없는 매개변수가 뒤에 오면 안된다
# 함수호출시 순서를 기준으로 변수에 할당하기 때문에
# 기본값설정이 되어있는게 나중 순서로 와야 호출 시 명확하게 변수에 할당할 수 있다.
# def greet2(name="친구", age):  # 에러
#     print(age, name)
# 호출시 age가 20이라고 생각하고 greet2(20) 호출하면, 컴퓨터는 이 20을 name이라고 생각하게 된다.
# 그럼 기본값을 설정한 이유가 없다 -> 이런 모호함을 없애기 위해서 에러를 발생하게 설계
