# any , all
any([False, False, True])  # 하나라도 True면, True
all([True, True, False])  # 하나라도 False면, False

# list comprehension : 리스트를 간결하게 조작해서 생성하는 문법
# [연산식 for 변수 in 반복가능한자료형 (if 조건)]

list1 = [1, 2, 3, 4, 5, 6]
list2 = []
for num in list1:
    list2.append(num**2)

print(list2)
list3 = [num**2 for num in list1]
print(list3)

list4 = [num for num in list1 if num % 2 == 0]
print(list4)

# 실습) 문자열들 중에서 길이다 3이하만 추출
words = ["hi", "python", "go", "hello", "world"]
print([word for word in words if len(word) <= 3])


# 이중 for문

a = [1, 2]
b = [10, 100]
# 두 리스트의 모든 곱셈 조합 결과
result = []
for num1 in a:
    for num2 in b:
        result.append(num1 * num2)

print(result)
print([num1 * num2 for num1 in a for num2 in b])

grades = ["5학년", "6학년"]
classes = ["A반", "B반"]
print([f"{grade}-{classe}" for grade in grades for classe in classes])

matrix = [[1, 2, 3], [4, 5, 6]]

flat = [num for row in matrix for num in row]
print(flat)


# 비밀번호 8자 이상, 숫자가 포함
# password = input("비밀번호 입력하세요 >>")
# if len(password) < 8:
#     # 8자 이하입니다 에러 발생
#     pass
#
# is_include_number = False
# for char in password:
#     if char.isdecimal():
#         is_include_number = True
#
# if not is_include_number:
#     # 숫자가 포함되어야 합니다 에러 발생
#     pass
#
# # 하나라도 true면 true!
# if not any([char.isdecimal() for char in password]):
#     # 숫자가 포함되어야 합니다 에러 발생
#     pass

# enumerate
names = ["홍길동", "김길동", "박길동"]
for index, name in enumerate(names):
    print(f"{index}: {name}")

# zip : 리스트 두개를 병렬 처리 시킬때 유용
a = [1, 2, 3]
b = ["a", "b", "c"]
for num, char in zip(a, b):
    print(f"{num}: {char}")

# 실습) 객관식 점수 매기기
answer = [3, 2, 5, 4, 2, 5, 4, 2, 1, 3]
# 홍길동이 제출한 답지
test_result = [3, 2, 2, 4, 3, 5, 3, 2, 2, 3]
# 한문제 다 10점으로 생각해서,
# 홍길동이 제출한 답지는 몇점인지 계산하여 출력

score = 0
for ans, res in zip(answer, test_result):
    if ans == res:
        score += 10

print(score)

result = [10 for ans, res in zip(answer, test_result) if ans == res]
score = sum(result)

print(f"정답 수:{len(result)}, 총점:{score}")
