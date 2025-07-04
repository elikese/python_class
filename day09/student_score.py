"""
학생들의 성적을 관리하는 시스템을 만들어보겠습니다.
여러 개의 함수를 만들어서 조합해보는 연습을 해보세요.

요구사항:
1. 학생 정보를 입력받는 함수
2. 성적을 계산하는 함수 (평균, 등급)
3. 성적표를 출력하는 함수 (성적 상세, 평균, 등급)
"""

# 학생 데이터 저장용 리스트
students = []

# 1단계: 학생 정보 입력 함수
def input_student_info():
    """학생 정보를 입력받아서 딕셔너리로 반환하는 함수"""
    print("=== 학생 정보 입력 ===")
    name = input("학생 이름: ")

    # 과목별 점수 입력
    korean = int(input("국어 점수: "))
    english = int(input("영어 점수: "))
    math = int(input("수학 점수: "))

    # 학생 정보를 딕셔너리로 만들기
    student = {
        'name': name,
        'korean': korean,
        'english': english,
        'math': math
    }

    return student

# 2단계: 평균 계산 함수
def calculate_average(korean, english, math):
    """세 과목 점수를 받아서 평균을 계산하는 함수"""
    total = korean + english + math
    average = total / 3
    return round(average, 1)  # 소수점 1자리까지

# 3단계: 등급 계산 함수
def calculate_grade(average):
    """평균 점수를 받아서 등급을 반환하는 함수"""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# 4단계: 성적표 출력 함수
def print_report_card(student):
    """학생 정보를 받아서 성적표를 출력하는 함수"""
    name = student['name']
    korean = student['korean']
    english = student['english']
    math = student['math']

    # 평균과 등급 계산
    average = calculate_average(korean, english, math)
    grade = calculate_grade(average)

    # 성적표 출력
    print(f"\n📋 {name}님의 성적표")
    print("=" * 30)
    print(f"국어: {korean}점")
    print(f"영어: {english}점")
    print(f"수학: {math}점")
    print("-" * 30)
    print(f"평균: {average}점")
    print(f"등급: {grade}등급")
    print("=" * 30)