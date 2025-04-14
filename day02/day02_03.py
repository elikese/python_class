# 제어문 (조건문 + 반복문)

# 조건문 (python엔 switch문 없음)
# if(bool자료형):
#   true일때 코드실행블럭 (들여쓰기 주의)
# elif(bool자료형):
#   true일때 코드실행블럭 (들여쓰기 주의)
# else:
#   그 외의 조건일때(=아주 조건들과 맞지 않을 때) 코드실행 블럭

# if ~ elif ~ else : 순차적으로 검사(위 -> 아래), 조건이 맞으면 해당 코드 블럭을 실행하고 탈출.
# 팁)) 순차적 검사 -> 조건이 점점 좁혀지는 방식으로 설계 되어야 한다.(조건이 정렬 되어야 함).(필터링)

# 조건이 정량적일때(숫자)
age = 10
if age >= 20:
    print("성인")
elif age >= 17:
    print("고등학생")
elif age >= 14:
    print("중학생")
elif age >= 8:
    print("초등학생")
else:
    print("미취학아동")

# 조건이 논리적일 때
# 특정 조건 코드 블럭이 실행된다는건, 이전 조건이 False라는 것

is_submitted = True
is_late = True
is_cheated = False

if not is_submitted:
    print("미제출")
elif is_cheated:
    print("부정행위")
elif is_late:
    print("지각 제출")
else:
    print("정상 제출")

is_logged_in = True
is_manager = False
is_banned = False

if not is_logged_in:
    print("로그인 해주세요")  # 로그인 여부가 최우선 (제일 먼저 체크)
elif is_banned:
    print("접근이 차단된 사용자입니다")  # 로그인했지만 차단된 경우
elif is_manager:
    print("관리자 페이지에 접근합니다")  # 로그인했고 차단 안 됐고 관리자일 때
else:
    print("일반 사용자 페이지에 접근합니다")  # 나머지는 일반 사용자

# 당연히 if문은 중첩이 됩니다.

if is_submitted:
    print("제출")
    if is_cheated:
        print("부정행위")
    elif is_late:
        print("지각 제출")
else:
    print("미제출")

# 논리적으로 오류가 없으면, 정답은 없습니다. -> 가독성, 코드관리의 측면에서 고민할 단계

# 실습3) bmi 계산기
# bmi = 체중(kg) / 신장(m)*신장(m)
# 18.5 미만 -> 저체중 / 18.5 이상 25 미만 -> 정상 / 25 이상 30미만 -> 과체중 / 30 이상 비만
# input을 통해 체중과 신장을 입력받아, bmi를 계산하여,해당하는 상태를 출력하시오

weight = float(input("체중을 입력하세요(kg):"))
height = float(input("신장을 입력하세요(cm):")) // 100
bmi = weight / (height**2)

# bmi는 소숫점 2째리에서 반올림하셔야 합니다. round() 사용!
rounded_bmi = round(bmi, 2)

if bmi >= 30:
    print("비만")
elif bmi >= 25:
    print("과체중")
elif bmi >= 18.5:
    print("정상")
else:
    print("저체중")
