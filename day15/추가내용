"""
any(), all(), zip() 학습 자료
"""

# ============================================
# 1. any() - True가 하나라도 있으면 True
# ============================================

# "True in [조건들]"과 같은 의미

numbers = [1, 3, 5, 8]

# 짝수가 하나라도 있는가?
results = [n % 2 == 0 for n in numbers]  # [False, False, False, True]
print("any():", any(results))  # True
print("True in:", True in results)  # True (같은 결과!)


# 예시: 가위바위보 승리 조건
나의선택 = "가위"
컴퓨터선택 = "보"

승리조건1 = 나의선택 == "가위" and 컴퓨터선택 == "보"
승리조건2 = 나의선택 == "바위" and 컴퓨터선택 == "가위"
승리조건3 = 나의선택 == "보" and 컴퓨터선택 == "바위"

# 방법 1: True in []
승리조건들 = [승리조건1, 승리조건2, 승리조건3]
print("승리?", True in 승리조건들)  # True

# 방법 2: any() (더 명확!)
print("승리?", any(승리조건들))  # True


# ============================================
# 2. all() - 모두 True여야 True
# ============================================

# "False not in [조건들]"과 같은 의미

numbers = [2, 4, 6, 7]

# 모두 짝수인가?
results = [n % 2 == 0 for n in numbers]  # [True, True, True, False]
print("all():", all(results))  # False
print("False 없음?:", False not in results)  # False (같은 결과!)


# 예제: 모두 합격인가?
scores = [85, 92, 78, 65]
pass_check = [score >= 60 for score in scores]
print("모두 합격?", all(pass_check))  # True


# ============================================
# 3. zip() - 여러 리스트 묶기
# ============================================

# 정답과 제출답안 비교
answer = [3, 2, 5, 4, 2]
test = [3, 2, 2, 4, 3]

# 기존 방식
correct = []
for i in range(len(answer)):
    correct.append(answer[i] == test[i])
print(correct)  # [True, True, False, True, False]

# zip 사용
correct = [ans == my for ans, my in zip(answer, test)]
print(correct)  # [True, True, False, True, False]

score = sum(correct) * 10
print("점수:", score)  # 30점


# ============================================
# 4. 종합 예제
# ============================================

# 학생별 점수
names = ["김철수", "이영희", "박민수"]
scores = [85, 42, 90]

# 1) 합격자가 있는가? (any)
has_pass = any(score >= 60 for score in scores)
print("합격자 있음?", has_pass)  # True

# 2) 모두 합격인가? (all)
all_pass = all(score >= 60 for score in scores)
print("모두 합격?", all_pass)  # False

# 3) zip으로 이름과 점수 묶기
for name, score in zip(names, scores):
    print(f"{name}: {score}점")


# ============================================
# 핵심 정리
# ============================================

# any() = True가 하나라도 → True (OR)
# all() = 모두 True → True (AND)
# zip() = 여러 리스트 동시 처리
