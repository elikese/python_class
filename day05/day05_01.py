# 컬렉션 자료형 복습
# 리스트 : 불변형 X, 순서 O, 중복 O, 대괄호[1,2,3,4]
# 튜플 : 불변형 O, 순서 O, 중복 O, 소괄호(1,2,3,4)
# 딕셔너리 : 불변형 X, 순서 O, key 중복 X, 중괄호에 키:밸류{"이름" : "홍길동"}
# 셋 : 불변형 X, 순서 X, 중복 X, 중괄호 {1,2,3,4}

# 반복문 : 동일한 패턴의 코드를 여러번이 아니라 한번에 작성 하기 위해서 사용 (for문, while문)
"""
for 요소 in 전체:
    코드(들여쓰기 주의)
"""
# 전체 -> 컬렉션 자료형, range(), 문자열 등.  *(참고) __iter__() 가 정의되어 있는 것들은 가능
# 요소 -> 순서대로 대입 받는 "변수"
# 한번 반복마다 for문에 들여쓴 코드가 실행 된다.

숫자리스트 = [0, 1, 2, 3, 4]
for 숫자 in 숫자리스트:
    print(숫자, end=" ")

# 첫 반복때 숫자라는 변수에는 0이라는 숫자가 대입된다.
# 두번째 반복때 숫자라는 변수에는 1이라는 숫자가 대입된다.


print()
총합 = 0
for 숫자 in 숫자리스트:
    총합 = 총합 + 숫자

print(f"총합:{총합}")

# range(): 숫자가 순서대로 들어있는 가짜리스트를 만들어 준다. -> 리스트가 아님(리스트 처럼쓰려면 list로 형변환)
# range(a_pakage,b_pakage) -> a부터 b미만 [a_pakage,a_pakage+1,a_pakage+2,.....,b_pakage-1]
# range(n) = range(0,n) -> 0부터 n미만 [0,1,2,3,4,......,n-1]

# 리스트로 형변환
형변환_range = list(range(10))
print(형변환_range)

for 숫자 in range(10):
    print(숫자, end=" ")  # 0,1,2,3,4...

print("\n----------")

# 1부터 50까지 홀수,짝수 나누어 담기
홀수, 짝수 = [], []
for 숫자 in range(1, 51):
    if 숫자 % 2 == 0:
        짝수.append(숫자)
    else:
        홀수.append(숫자)

print(f"홀수:{홀수}")
print(f"짝수:{짝수}")

# 실습)1부터 50까지 홀수는 홀수끼리 더하여 홀수합을
# 짝수는 짝수끼리 더하여 짝수합을 구하여 출력해주세요
홀수합, 짝수합 = 0, 0

for 숫자 in range(1, 51):
    if 숫자 % 2 == 0:
        짝수합 += 숫자
    else:
        홀수합 += 숫자

print(f"짝수합은 {짝수합}이고, 홀수합은 {홀수합}입니다")

for _ in range(5):
    print("안녕하세요")
# i는 안써도됨 -> i대신에 _로 바꾸는게 국룰

# 별찍기
for _ in range(5):
    print("*", end="")

"""
print(*, end="")
print(*, end="")
print(*, end="")
print(*, end="")
print(*, end="")
같은코드를 5번 반복한 것
"""
print()

# 2중 for문
for i in range(2):  # 바깥 반복문
    print(f"[i={i}] 줄 시작")
    for j in range(3):  # 안쪽 반복문
        print(f"  j={j} → 출력")
    print(f"[i={i}] 줄 끝")
    print()

"""
바깥 반복 한번당, 안쪽 반복이 전부 도는 구조
i = 0 -> j = 0, j = 1, j = 2
i = 1 -> j = 0, j = 1, j = 2
"""

# 구구단
for 단 in range(2, 10):
    print(f"{단}단 시작!")
    for 숫자 in range(2, 10):
        print(f"{단}*{숫자}={단*숫자}", end="")
    print()
    print(f"{단}단 끝!")

# 별찍기(5*5)
for _ in range(5):  # 바깥반복문 -> 세로
    for _ in range(5):  # 안쪽반복문 -> 가로
        print("*", end="")

    print()
"""
for _ in range(5):
    print("*", end="")

결과 : *****
이걸 5번 반복하려면?

for _ in range(5):
    for _ in range(5):
        print("*", end="") # *****
    print() # 줄바꿈
"""

"""
아래를 출력해주세요!

****
****
****
****
****
****

6줄, 각 줄마다 별 4개
"""

"""
*
**
***
****
*****
을 출력해보세요!
"""
n = 10
for i in range(n):
    for j in range((n - 1) - i):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
