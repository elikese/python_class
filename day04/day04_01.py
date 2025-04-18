# 튜플 : 수정과 삭제가 안되는 리스트 -> 변경이 안되는 리스트
# 한번 데이터가 들어오면 "불변(immutable)" -> 원본이 훼손이 안된다.
# 물론 복사해서 사용할 수는 있다!(슬라이싱)

이름들 = ("철수", "영희", "민수")
숫자들 = (1, 2, 3, 4, 5)
짬뽕 = (1, False, "철수")

# 요소가 하나일떄는 쉼표를 적어준다.
하나만있는튜플 = ("하나",)

튜플_냉장고 = ("사과", "바나나", "포도", "수박", "수박")

# 튜플_냉장고[0] = "포도"  # 변경불가능
사과위치 = 튜플_냉장고.index("사과")
print(사과위치)
수박갯수 = 튜플_냉장고.count("수박")
print(수박갯수)

# 슬라이싱은 가능합니다.
# 왜? 슬라이싱은 원본을 건드리지 않고, 해당영역을 복사해서 새로 만들어 주기 떄문
문자열_원본 = "hello world"
슬라이싱한_문자열 = 문자열_원본[:5]
print(f"슬라이싱 확인: {슬라이싱한_문자열}")
print(f"원본 확인: {문자열_원본}")

리스트_원본 = [0, 1, 2, 3, 4]
슬라이싱한_리스트 = 리스트_원본[:2]
print(f"슬라이싱 확인: {슬라이싱한_리스트}")
print(f"원본 확인: {리스트_원본}")

튜플_원본 = (0, 1, 2, 3, 4)
슬라이싱한_튜플 = 튜플_원본[:2]
print(f"슬라이싱 확인: {슬라이싱한_튜플}")
print(f"원본 확인: {튜플_원본}")

# 튜플 언패킹
홍길동씨 = ("홍길동", "조선", 30, "남자", True)
이름, 국적, 나이, 성별, 결혼여부 = 홍길동씨
print(이름, end=" ")
print(국적, end=" ")
print(나이, end=" ")
print(성별, end=" ")
print(결혼여부)
# 이스케이프(복습) -> \(enter키 위에)
# \n: 엔터(줄바꿈),
# \t: 4칸띄움(탭)


# 값 스왑
a = 10
b = 20
"""
다른언어는? 두 변수가 값을 바꾸려면 하나의 변수가 추가로 필요함
int a = 10;
int b = 20;
int temp = a;
a = b;
b = temp;
"""
a, b = b, a
print(f"a={a}, b={b}")

a = 10
b = 20
c = 30
d = 40
a, b, c, d = d, c, b, a

# 실습) 주어진 좌표가 몇사분면에 있는지 판별해서 출력해주세요!
# if문 사용!
# 원점, x축, y축 위에 있는 경우(x=0 or y=0인경우) 고려 x

좌표 = (3, -3)
x, y = 좌표
if x > 0 and y > 0:
    print("1사분면")
elif x < 0 and y > 0:
    print("2사분면")
elif x < 0 and y < 0:
    print("3사분면")
elif x > 0 and y < 0:
    print("4사분면")

if x > 0 and y > 0:
    print("1사분면")
if x < 0 and y > 0:
    print("2사분면")
if x < 0 and y < 0:
    print("3사분면")
if x > 0 and y < 0:
    print("4사분면")

if x > 0:
    if y > 0:
        print("1사분면")
    elif y < 0:
        print("4사분면")
elif x < 0:
    if y > 0:
        print("2사분면")
    elif y < 0:
        print("3사분면")
