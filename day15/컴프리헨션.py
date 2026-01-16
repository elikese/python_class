"""
컴프리헨션(Comprehension) 학습 자료
"""

# ============================================
# 1. 리스트 컴프리헨션 - 기본
# ============================================

# 기존 방식 vs 컴프리헨션
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("기존:", squares)  # [1, 4, 9, 16, 25]

squares = [i ** 2 for i in range(1, 6)]
print("컴프리헨션:", squares)  # [1, 4, 9, 16, 25]


# 기본 형태: [표현식 for 변수 in 반복가능객체]
fruits = ["apple", "banana", "kiwi"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # ['APPLE', 'BANANA', 'KIWI']


# ============================================
# 2. 리스트 컴프리헨션 - 조건문
# ============================================

# 데이터의 일부분 필터 + 변환
# if만 사용: [표현식 for 변수 in 반복가능객체 if 조건]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print("짝수:", evens)  # [2, 4, 6, 8, 10]

# 전체데이터 변환
# if-else 사용: [참값 if 조건 else 거짓값 for 변수 in 반복가능객체]
scores = [85, 42, 90, 55, 78]
results = ["합격" if score >= 60 else "불합격" for score in scores]
print(results)  # ['합격', '불합격', '합격', '불합격', '합격']


# ============================================
# 3. 딕셔너리 컴프리헨션 - 기본
# ============================================

# 기존 방식 vs 컴프리헨션
square_dict = {}
for i in range(1, 6):
    square_dict = update({
      i : i**2
    })
print("기존:", square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

square_dict = {i: i ** 2 for i in range(1, 6)}
print("컴프리헨션:", square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 기본 형태: {하나씩 들어갈 키: 하나씩 들어갈 값 for 변수 in 반복가능객체}
fruits = ["apple", "banana", "kiwi"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)  # {'apple': 5, 'banana': 6, 'kiwi': 4}


# ============================================
# 4. 딕셔너리 컴프리헨션 - 조건/변환
# ============================================

# 조건문 사용
scores = {"김철수": 85, "이영희": 42, "박민수": 90, "최지우": 55}
passing = {name: score for name, score in scores.items() if score >= 60}
print("합격자:", passing)  # {'김철수': 85, '박민수': 90}


# 키↔값 교환
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("교환:", swapped)  # {1: 'a', 2: 'b', 3: 'c'}


# 값 변환
prices = {"사과": 1000, "바나나": 1500}
discounted = {item: price * 0.9 for item, price in prices.items()}
print("10% 할인:", discounted)  # {'사과': 900.0, '바나나': 1350.0}


# ============================================
# 5. 실전 예제 - 클래스와 컴프리헨션
# ============================================

# Student 클래스 정의
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return f"Student(id={self.id}, name={self.name})"


# 학생 객체 리스트 생성
students = [
    Student(1, "김철수"),
    Student(2, "이영희"),
    Student(3, "박민수")
]

print("원본:", students)

# 리스트 컴프리헨션으로 ID를 "st1", "st2" 형태로 변환
students_new = [Student(f"st{s.id}", s.name) for s in students]
print("변환:", students_new)
# [Student(id=st1, name=김철수), Student(id=st2, name=이영희), ...]


# 학생 평균 구하기 (원래 예제)
student_scores = {
    "김철수": [85, 90, 78],
    "이영희": [92, 88, 95],
    "박민수": [45, 50, 55]
}

averages = {name: sum(scores) / len(scores) 
            for name, scores in student_scores.items()}
print("평균:", averages)

# 합격자만 (평균 60점 이상)
passing = {name: avg for name, avg in averages.items() if avg >= 60}
print("합격:", passing)
