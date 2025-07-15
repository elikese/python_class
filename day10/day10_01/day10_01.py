# file
# 메모리(ram) - 휘발적(실행도중에만 유효) : 칠판에 적었다가 다시 지우는 것
# 파일(HDD / SSD) - 반영구적 보존 : 노트에 필기해서 보관

file = open("./example.txt", "w", encoding="utf-8")
file.write("Hello World")
file.close()

# open(경로, 파일모드, encoding)
"""
- 경로(절대경로, 상대경로)
절대경로(c:\python\python_class\example.txt)
상대경로('../' , './') -> ../ 현재 파일의 위로가기, ./ 현재파일의 폴더위치
day10_01.py과 같은 위치에 example.txt가 생겼으니
day10_01.py에서 './example.txt'로 접근 가능
day08_01.py에서 '../day09/example.txt로 접근가능

- 파일모드
r:read , w:write, a_pakage:append
t:text(문자열로만 이루어진 파일), b_pakage:binary(이미지, jpg, mp3, exe)
보통은 rt, wt, rb, wb 같이 조합해서 사용합니다. t는 생략가능(t가 기본값)

- encoding
파일은 사실 컴퓨터가 알아듣게 저장된 것(숫자로 이루어 져있다)
글자들을 숫자로 바꿀때 필요한 규칙같은 것
uff-8에서 '가' -> 44032
이미지 또한, 숫자들로 이루어 져 있습니다.
대표적으로 사용되는게 ascii, utf-8(웹표준), 옛날(euc-kr), cp949(윈도우os, 관공서)
"""
# 읽기
f = open("./example.txt", "r", encoding="utf-8")
a = f.read()  # 한번에 다 읽기(정말 큰 파일이라면 메모리 부담)
f.close()  # close를 해줘야 메모리에서 f가 사라짐(수동)
print(a)

# 들여쓰기가 된 곳까지 코드가 모두 진행되면 자동으로 close해줌(with)
# 원래는 open으로 만든 file을 변수에 대입해서 사용했는데 as로 대체
with open("./example.txt", "r", encoding="utf-8") as f:
    a = f.read(10)  # 10바이트 읽어오기
    print(a)
    a = f.read(10)  # 마지막 읽은 위치로 부터 추가로 10바이트 읽어옴
    # -> 지금까지 읽은 위치를 내부적으로 저장하고 있다(커서)
    print(a)
    f.seek(0, 0)  # 커서 초기화
    print("-----------------")
    a = f.readline()  # \n 이스케이프 문자 인식해서 한줄씩 읽어온다
    print(a, end="")  # \n 까지 읽어 오는거라서 print의 end옵션을 통해 개행x
    a = f.readline()
    print(a, end="")
    f.seek(0, 0)

with open("./example.txt", "r", encoding="utf-8") as f:
    a = f.readlines()  # 한줄단위로 끊어서 리스트로 만들어 준다
    print(a)

# 쓰기
# w는 덮어쓰기
with open("./example2.txt", "w", encoding="utf-8") as f:
    f.write("python\n")

# a는 파일의 마지막부터 이어쓰기
with open("./example2.txt", "a", encoding="utf-8") as f:
    f.write("python!\n")

# writeLines : 리스트를 쓰기로
with open("./example3.txt", "w", encoding="utf-8") as f:
    fruits = ["apple", "banana", "cherry", "melon"]
    f.writelines(fruits)

# 이미지
half = 0
data = None
with open("./img.png", "rb") as f:
    data = f.read()
    print(data[:100])
    half = len(a) // 2


# txt말고, csv, xml, JSON
# JSON - 웹에서 데이터를 주고받는 용도로 사용 됨
"""
{
    "name": "홍길동",
    "age": 30,
    "is_student": false
}
"""

import json

dict_data = {
    "name": "홀길동",
    "age": 30,
}

with open("./data.json", "w", encoding="utf-8") as f:
    # dump(dict자료, f(파일), ensure_ascii:한글이 깨지지않게, indent(들여쓰기)
    json.dump(dict_data, f, ensure_ascii=False, indent=4)

# json과 dict의 차이?
# json의 key는 반드시 "문자열", value는 숫자, 문자열, list, dict 가능
# dict의 key는 문자열, 정수, 튜플....(immutable:불변형)가능 value는 파이썬의 모든 자료형이 가능
# dict -> JSON으로 가려면, key의 자료형들을 문자열로 바꿔줘야한다.
"""
{
1: "사과",
2: "바나나",
(1,2): "에드워드리 음식점",
}

JSON으로 변환시

{
"1": "사과",
"2": "바나나",
}

이 모든 과정을 import한 json 모듈이 알아서 해준다.
우리는 모듈에 이미 작성된 함수만 호출하면 된다.(dump, load)
"""

with open("./data.json", "r", encoding="utf-8") as f:
    new_dict_data = json.load(f)
    print(new_dict_data)
