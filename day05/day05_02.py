# break & continue
숫자들 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# break : for문 탈출!
for 숫자 in 숫자들:
    print(숫자, end=" ")
    if 숫자 == 5:
        print()
        print("숫자 5 찾았어요! for문 탈출!")
        break  # for문 탈출한다(코드 블럭 밖으로)
        print("이 코드는 실행되지 않습니다")

# continue : for문 반복 중 해당 반복만 스킵할때

print("------------")
for 숫자 in 숫자들:
    if 숫자 == 5:
        print()
        print("숫자 5 찾았어요! 바로 다음 반복으로 이동!")
        continue
    print(숫자, end="")
print()
print("------------")

# 문자열과 반복문
# 문자열도 순서가 있다. -> 순회가 가능하다. *참고) 문자열도 __iter__()가 존재하기 때문에

문자열 = "Hello World"
for 문자 in 문자열:
    print(문자, end=",")

print()
for 문자 in 문자열:
    if 문자.isupper():
        print(문자, end=",")

print()
for 문자 in 문자열:
    if 문자.islower():
        print(문자, end=",")
print()

# 리스트와 반복문
냉장고 = ["계란", "우유(상함)", "김치", "사과", "치즈(상함)", "된장국"]

# 상한 음식만 출력
for 식품 in 냉장고:
    if "상함" in 식품:
        print(식품)

# 실습) 상한 음식만 빼고 출력 (continue 사용)
for 식품 in 냉장고:
    if "상함" in 식품:
        continue
    print(식품)

# 상한 음식 뒤에 "(상함)" 삭제하기
for 식품 in 냉장고:
    if "상함" in 식품:
        식품 = 식품[
            :-4
        ]  # 식품은 대명사, 원본이 아니다. 지금 반복이 몇번 째 반복인지를 알려주는 변수가 필요

# enumerate(): 매 반복마다 (인덱스, 값) 튜플형태로 만들어준다.
# 인덱스, 식품 = (1, "계란") # 튜플 언패킹
# 인덱스, 식품 = (2, "우유(상함)") # 튜플 언패킹
# 인덱스, 식품 = (3, "김치") # 튜플 언패킹
for 인덱스, 식품 in enumerate(냉장고):
    print(f"{인덱스} : {식품}")

# 방법1
for 인덱스, 식품 in enumerate(냉장고):
    if "상함" in 식품:
        냉장고[인덱스] = 식품[:-4]

# 방법2
for 인덱스, 식품 in enumerate(냉장고):
    if "상함" in 식품:
        냉장고[인덱스] = 식품.replace("(상함)", "")
print(냉장고)

# 실습) 과일박스에서 홀수 인덱스에만 있는것만 출력해 주세요
과일박스 = ["사과", "바나나", "체리", "포도", "망고"]
# 1번: 바나나, 3번: 포도
for 인덱스, 과일 in enumerate(과일박스):
    if 인덱스 % 2 != 0:
        print(f"{인덱스}번 인덱스 과일: {과일}")
