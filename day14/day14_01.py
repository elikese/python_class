# 예외: 예상하지 못한 ERROR

# 빨간줄 : SyntaxError
# 예외 종류
# 1. SyntaxError: 문법에러 (코드 아래에 빨간 줄)
# 2. TypeError: 타입이 맞지 않은 '연산'시 발생
a = "hello"
b = 3
# print(a + b)  # TypeError: 문자열 + 숫자 -> 타입이 맞지않는 연산

# 3. NameError: 선언되지 않은 변수 사용 시 발생
# print(x)
x = 3

# 4. IndexError: 인덱스 범위를 벗어났을때
list = [1, 2, 3]
# print(list[100])  # 범위 초과

# 5. KeyError: dict에 없는 키를 접근할 때
dict_data = {"name": "홍길동", "age": 20}
print(dict_data["gender"])  # gender라는 키는 없음

# 6. ValueError: 타입은 맞는데, 값이 부적절한 경우
a = "abc"
int(a)
# int()는 문자열 받을 수 있음, 근데 그 값이 숫자처럼 생긴 문자열이어야 됨
