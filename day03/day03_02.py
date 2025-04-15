# 리스트
# 문자열 -> 파이썬에서는 리스트의 사촌(공통점이 많다)

last_names = ["김", "이", "박"]  # str 리스트
numbers = [1, 2, 3, int(4.0), int("5")]  # int 리스트
bools = [True, False, "김" == "김", 1 >= 2]  # bool리스트

str_example = "안녕하세요"
list_example = ["안", "녕", "하", "세", "요"]
print(str_example[0])
print(list_example[0])
print(str_example[-1])
print(list_example[-1])
# str처럼 list는 인덱스로 순서가 존재하는 자료형.
# indexing(a[0]), slicing(a[0:5]), len(a), in 연산자, (+,*)연산자, count 가능.
# 하지만, 두개의 자료형이 똑같은 것은 아닙니다.

# 슬라이싱
print(str_example[:2])  # 문자열을 잘라서 줌
print(list_example[:2])  # 리스트를 잘라서 줌

# len() : 길이
print(len(str_example))  # 문자열 길이
print(len(list_example))  # 리스트 길이

# in 연산자 : 존재 체크
print("안" in str_example)  # 문자열에 "안" 문자가 있는가?
print("안" in list_example)  # list에 "안" 이 있는가?

# 리스트에는 아무거나 넣을 수 있습니다.
mix_type_list = ["김", 1, 5.5, True, ["점심", "저녁"]]

fruits = ["사과", "바나나", "포도", "수박"]

# 요소 접근(인덱싱)
print(fruits[0])  # 사과
print(fruits[-1])  # 수박
print(fruits[0][0])  # 사

# 요소 변경
fruits[0] = "토마토"
print(fruits)

# 요소 추가
fruits.append("사과")
print(fruits)  # 마지막 자리에 추가
fruits.insert(0, "망고")
print(fruits)  # 특정 위치에 추가(기존 요소들은 뒤로 밀려남)

# 요소 삭제
fruits.remove("망고")  # 특정 값 삭제

fruits.pop()  # 특정 인덱스(위치) 요소 삭제, 생략할 경우 마지막 요소 삭제
del fruits[1]  # 특정 인덱스(위치) 요소 삭제

# pop은 꺼내오는것 , del은 삭제
fruits2 = ["사과", "바나나", "수박", "포도"]
pop_fruits2 = fruits2.pop()  # 포도 꺼내옴
print(pop_fruits2)

# 리스트 더하기
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
# 새 list를 만들어서 list1과 list2를 담아서 줌 -> 원본(list1, list2)변경된게 아님

list1.extend(list2)
print(list1)
# list 자체가 바뀌는것 -> 원본(list1)이 변경됨

# 리스트 곱하기
print(list1 * 2)
