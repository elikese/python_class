# replace
a = "life is too short you need python"
a_replace = a.replace(" ", "_")
print(a_replace)

# strip
a = "**특가 할인행사**"
print("a_strip", a.strip("*"))
print("a_rstrip", a.rstrip("*"))
print("a_lstrip", a.lstrip("*"))

a = "박:화목"
a_split = a.split(":")
print(a_split)

print(a_split[0])
print(a_split[1])

first_name = a_split[1]
last_name = a_split[0]

print(last_name + first_name)

# input()을 통해 email을 변수에 저장한다. 예) python@gmail.com
# split() 활용하여 email 아이디만 추출하여 print해보세요.

a = "hello world!"
# 대문자 / 소문자 변환
print("a_upper:", a.upper())  # 전체 문자열 대문자로
print("a_lower:", a.lower())  # 전체 문자열 소문자로

# capitalize
print("a_capitalize:", a.capitalize())
print("a_capitalize:", a[:1].upper() + a[1:])

# count
print("a_count:", a.count("d", 6, 10))
print("a_count:", a[6:10].count("d"))

# in 연산자
print("존재여부확인:", "h" in a)
print("존재여부확인:", "hello" in a)

# 문자열의 처음과 끝이 무엇으로 시작하는지 검사
print("a_startswith:", a.startswith("he"))
# print("a_startswith:", a_pakage[:2] == "he")
print("a_endswith:", a.endswith("d!"))
# print("a_endswith:", a_pakage[-2:] == ("d!"))

name = "홍길동"
print("성씨가 김이박입니까?", name[:1] == "김" or name[:1] == "이" or name[:1] == "박")
list_last_name = ["김", "이", "박"]
print("성씨가 김이박입니까?", name.startswith(tuple(list_last_name)))

# 멀티라인
multiline_str = """
문자열
여러줄
저장
"""
# 멀티라인도 format() / fstring 가능하다.

print("-멀티라인시작-")
print(multiline_str)
print("-멀티라인종료-")
# 문자열에서 사용하는 이스케이프 문자
# \n: 엔터(줄바꿈),
# \t: 4칸띄움(탭),
# \', \"": ' , "를 문자로서 사용할 때

real_multiline_str = "\n문자열\n여러줄\n저장\n"
print("-멀티라인시작-")
print(real_multiline_str)
print("-멀티라인종료-")

"""
멀티라인은. 공식적으로 주석은 아니지만,
변수에 할당만 안하면, 주석처럼 사용할 수 있습니다.
원래는 함수설명(docstring)으로 사용하려고 만든 기능 
"""
