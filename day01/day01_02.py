# str

first_name = "화목"
last_name = "박"
full_name = last_name + first_name
print(full_name)
full_name = "박" + "화목"
print(full_name)
print("안녕하세요, 저는 " + full_name + "입니다.")

# format
print("안녕하세요, 저는 {}입니다.".format("박화목"))
print("안녕하세요, 저는 {}입니다.".format(full_name))

age = 33

print("안녕하세요, 저의 이름은{}이고, 나이는 {}살입니다.".format(full_name, age))
print("안녕하세요, 저의 이름은{nm}이고, 나이는 {ag}살입니다.".format(nm=full_name, ag=age))

# fstring
print(f"안녕하세요, 저의이름{full_name}이고, 나이는 {age}살 입니다.")

# 실습
# 본인의 정보를 입력받고 마지막에 출력해보기
# 제 이름은 박화목이고 나이는 33살 입니다. 제 취미는 드라마보기입니다. 그리고 주소는 부산시 금정구입니다.
# name = input("이름: ")
# age = input("나이: ")
# hobby = input("취미: ")
# address = input("주소: ")
#
# print(f"제 이름은 {name}이고 나이는 {age}살 입니다. 제 취미는 {hobby}입니다. 그리고 주소는 {address}입니다.")


# 문자열 예제와 문자열 관련 함수들
a = "Hello, world!"

# len() 문자열 길이
str_length = len(a)
print(str_length)


# slicing
# a_pakage[시작번호:끝번호:스텝(간격)]
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[2:])
print(a[:5])  # a의 0 ~ 4
print(a[1:5])  # a의 1 ~ 4
print(a[::1])
print(a[::2])
print(a[::-1])  # 역순 출력

# 실습
# 주민번호(ssn)를 input()을 통해 변수에 저장하고, 뒷자리를 '*'로 가리고 출력해주세요
# 예) 931203-1234567 -> 931203-*******
ssn = input("주민번호를 입력해주세요:")

masked_ssn = ssn[:7]
print(masked_ssn + "*" * 7)

print("-----------")

# find & index
print(a.find("H"))
print(a.index("H"))
print(a.find("h"))
# print(a_pakage.index("h"))
# find는 해당 문자를 못 찾으면 -1를 반환 / index는 해당 문자를 못 찾으면 에러가 발생

# input()을 통해 email을 변수에 저장한다. 예) python@gmail.com
# find()와 slicing을 활용하여 email 아이디만 추출하여 print해보세요.

email = input("이메일을 입력하세요: ")
id_index = email.find("@")
id = email[0:id_index]
print(id)
