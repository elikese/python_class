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
