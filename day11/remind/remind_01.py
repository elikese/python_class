# 정수와 실수 예제
a = 10  # 정수(int) 변수 선언
b = 3.5  # 실수(float) 변수 선언
print(a + 5)  # 정수는 사칙연산이 가능 (결과: 15)
print(b * 2)  # 실수도 사칙연산 가능 (결과: 7.0)

# 문자열(str) 예제
name = "홍길동"  # 문자열 변수 선언 (따옴표로 감싼 텍스트)
greeting = "안녕하세요, " + name + "님!"  # 문자열 연결(Concatenation)
print(greeting)  # 결과: 안녕하세요, 홍길동님!

# 불리언(bool) 예제
is_open = True  # 불리언 변수 (True 혹은 False 값)
print(is_open)  # True 출력 (True는 참, False는 거짓을 의미)

# 형 변환 예제 (int, float, str, bool)
print(int(5.7))  # float -> int 변환 (소수점 버림, 결과: 5)
print(float("10"))  # str -> float 변환 (숫자 문자열을 실수로, 결과: 10.0)
print(str(100) + "원")  # int -> str 변환 후 문자열 연결 (결과: "100원")
print(bool(0), bool("안녕"))  # bool 변환 (0은 False, 빈 문자열 외의 값은 True)

#####################################################
# 조건문
age = 15  # 나이에 따라 다른 메시지 출력
if age >= 20:
    print("성인입니다.")
elif age >= 14:
    print("청소년입니다.")  # 앞의 조건이 거짓이고 age >= 14가 참인 경우 실행
else:
    print("어린이입니다.")  # 모든 위 조건이 거짓일 때 실행

# if문은 참(True)/거짓(False) 판단으로 실행 여부를 결정
# 파이썬에서는 0이나 빈 문자열("", []) 등은 False로 간주하고
# 그 외의 값은 True로 간주하여 조건문에서 활용할 수 있음
#####################################################
# 자료구조
# 리스트(list) - 순서가 있고 변경 가능(mutalble)
fruits = ["사과", "바나나", "체리"]
print(fruits[0])  # 인덱스로 접근 (결과: '사과')
fruits.append("포도")  # 요소 추가
print(fruits)  # ['사과', '바나나', '체리', '포도']

# 튜플(tuple) - 순서가 있고 **변경 불가(immutable)**
nums = (1, 2, 3)
# nums[0] = 10  # 오류: 튜플은 값을 변경할 수 없음
print(nums.count(2))  # 튜플에서 값 2의 개수 (결과: 1)

# 딕셔너리(dict) - 키-값 쌍으로 구성된 자료형
person = {"이름": "홍길동", "나이": 30}
print(person["이름"])  # 키를 사용해 값 접근 (결과: '홍길동')
person["직업"] = "학생"  # 새로운 키-값 추가
print(person)  # {'이름': '홍길동', '나이': 30, '직업': '학생'}

# 세트(set) - 순서 없고 중복 불가한 집합
unique_nums = {1, 2, 2, 3}
print(unique_nums)  # 중복된 2는 하나만 남음 (결과: {1, 2, 3})
unique_nums.add(4)  # 요소 추가
print(unique_nums)  # {1, 2, 3, 4}
print(unique_nums | {3, 5})  # 합집합 연산 (결과: {1, 2, 3, 4, 5})
#####################################################
# 반복문
# for문으로 1부터 5까지 합계 구하기
total = 0
for i in range(1, 6):  # range(1, 6) -> 1,2,3,4,5
    total += i
print(total)  # 결과: 15

# 리스트 요소 순회 예제
foods = ["햄버거", "피자", "샐러드"]
for item in foods:
    print(item)  # 각 요소를 출력

# break와 continue 사용 예제
for n in range(1, 10):
    if n == 5:
        break  # n이 5이면 반복문 종료
    if n % 2 == 0:
        continue  # n이 짝수이면 아래 코드 건너뛰고 다음 반복으로
    print(n, end=" ")  # 결과: 1 3 (5에서 종료되어 1과 3만 출력됨)
#####################################################
# 반복문
# while문 기본 예제: 5부터 1까지 출력
count = 5
while count > 0:  # 조건이 True인 동안 반복
    print(count)
    count -= 1  # 반복 변수를 변경 (감소)
# 출력: 5, 4, 3, 2, 1

# 무한 루프와 break 예제
n = 1
while True:  # 항상 True인 조건 -> 무한 루프
    print(n)
    n += 1
    if n == 5:
        break  # n이 5가 되면 루프 종료
# 출력: 1, 2, 3, 4

# continue를 사용한 예제: 1~10 중 3의 배수만 건너뛰기
m = 0
result_list = []
while m < 10:
    m += 1
    if m % 3 == 0:
        continue  # 3의 배수는 아래 코드 실행하지 않고 다음 반복으로
    result_list.append(m)
print(result_list)  # 결과: [1, 2, 4, 5, 7, 8, 10]


#####################################################
# 함수 정의 및 호출
def greet(name):
    print(f"안녕하세요, {name}님!")  # 이름을 받아 인사 메시지 출력


greet("철수")  # 함수 호출 -> "안녕하세요, 철수님!" 출력


# 반환값이 있는 함수
def add(x, y):
    return x + y  # 두 수의 합을 반환


result = add(3, 5)
print(result)  # 결과: 8 (add 함수의 반환값)


# 기본 매개변수 값이 있는 함수
def introduce(name, age=20):
    print(f"저는 {name}이고, 나이는 {age}살입니다.")


introduce("영희")  # age 인자를 생략하면 기본값 20 사용
introduce("민수", age=25)  # 기본값 대신 25 사용하여 출력


# 가변 인자 *args 예제 (여러 개의 숫자를 모두 더하는 함수)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_all(1, 2, 3, 4))  # 결과: 10 (1+2+3+4의 합)

#####################################################
# file 입 출력

# 텍스트 파일에 데이터 쓰기 (write)
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world!\n")  # 파일에 문자열 기록

# 텍스트 파일에서 데이터 읽기 (read)
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)  # 파일 내용 출력 (결과: Hello, world!)

# JSON 모듈 활용 - 파이썬 딕셔너리를 JSON 파일로 저장하고 불러오기
import json

data = {"이름": "홍길동", "나이": 30}

# JSON 파일로 저장 (쓰기)
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)  # 딕셔너리를 JSON 형식으로 기록

# JSON 파일에서 읽어오기
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)  # JSON 내용을 파싱하여 파이썬 객체(dict)로 불러옴

print(loaded)  # 결과 출력: {'이름': '홍길동', '나이': 30}
