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
