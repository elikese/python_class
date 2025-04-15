# 리스트
# 문자열 -> 파이썬에서는 리스트의 친척(비슷하다)

last_names = ["김", "이", "박"]  # str 리스트
numbers = [1, 2, 3, int(4.0), int("5")]  # int 리스트
bools = [True, False, "김" == "김", 1 != 2]  # bool리스트

str_example = "안녕하세요"
list_example = ["안", "녕", "하", "세", "요"]
print(str_example[0], list_example[0])
print(str_example[-1], list_example[-1])
# str처럼 list는 인덱스로 순서가 존재하는 자료형.
# indexing(a[0]), slicing(a[0:5]), len(a), in연산자, (+,*)연산자, count 가능.
# 하지만, 두개의 자료형이 정말 같은 것은 아닙니다.
print(str_example[:2], list_example[:2])

# 아무거나 넣을 수 있다.
mix_type_list = ["김", 1, 5, True, ["점심", "저녁"]]
