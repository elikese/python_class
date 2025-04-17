# 셋(set) {}
# 순서 X, 중복 X
# 집합 기억나세요? 집합이랑 똑같습니다. 합집합, 교집합, 차집합
과일 = {"사과", "바나나", "사과", "딸기"}
print(과일)  # 사과 중복이 안됨, 매번 실행할 때 마다 순서 바뀜

숫자들 = {1, 2, 3, 4, 5, 5}

# 요소 추가
숫자들.add(6)
print(숫자들)
# 여러개 한꺼번에 추가: update() -> update() 함수 안에는 리스트([]) 나 셋({})로 넣어줘 합니다.
숫자들.update({7, 8, 9, 10})

# 요소 삭제
# discard() / remove()
숫자들.discard(5)  # 5삭제, 요소가 없어도 아무일 없음
print(숫자들)
# 숫자들.remove(5)  # 5삭제, 요소가 없으면 keyError 발생
print(숫자들)

# pop() 무작위로 요소를 꺼내 온다
파란색 = {"파", "란", "색"}
print(파란색.pop())
# 알고리즘으로 무작위를 구현한것.
# print(숫자들.pop())
# 무작위가 컴퓨터에 존재할까요?(x) : 무작위처럼 보이게 만드는 것(100%가 아니면 무작위)

# 집합연산
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# 합집합 : 두 집합을 합쳐서 중복은 제거
print(a.union(b))
print(a | b)

# 교집합 : 두 집합에 중복만 골라냄
print(a.intersection(b))
print(a & b)

# 차집합 : 기존값에서 중복 제거한것
print(a.difference(b))
print(a - b)
print(a - (a & b))

# 실습)
수학강의_출석 = ["철수", "영희", "영수", "상호"]
과학강의_출석 = ["숙자", "철수", "찬호", "영희"]
# 1. 둘다 출석한 학생
# 2. 수학만 출석한 학생
# 3. 과학만 출석한 학생
# 출력해주세요!
print(set(수학강의_출석) & set(과학강의_출석))  # 둘다
print(set(수학강의_출석) - set(과학강의_출석))  # 수학만
print(set(과학강의_출석) - set(수학강의_출석))  # 과학만

# 실습) 맞팔한 사람들만 구해보세요
인스타_팔로잉 = {
    "민수": True,
    "철수": True,
    "지우": True,
    "나연": True,
}
팔로워 = {"정우", "민수", "나연"}
