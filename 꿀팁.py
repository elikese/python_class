import day01.day01_01

# 튜플 언패킹
홍길동씨 = ("홍길동", "조선", 30, "남자", True)
이름, 국적, 나이, 성별, 결혼여부 = 홍길동씨
print(이름)
print(국적)
print(나이)
print(성별)
print(결혼여부)

# any , all
any([False, False, True])  # 하나라도 True면, True
all([True, True, False])  # 하나라도 False면, False

# 리스트 언패킹
기차 = ["1호칸", "2호칸", "3호칸", "4호칸", "5호칸"]
맨앞칸, *중간칸들, 맨뒷칸 = 기차
print(f"맨앞칸={맨앞칸}, 중간칸들={중간칸들}, 맨뒷칸={맨뒷칸}")

# zip -> 리스트 두개를 동시 순회하는 것
# 따로 저장되어있던 연관된 리스트를 하나로 묶을때, 순회할 때
students = ["김철수", "박철수", "이철수"]
scores = [100, 90, 80]

for name, score in zip(students, scores):
    print(f"name={name}, score={score}")
result = dict(zip(students, scores))
print(result)

# 비교할 때(다른거 찾기)
기대값들 = [1, 2, 3, 4, 5]
실제값들 = [1, 2, 9, 4, 7]
for 기대값, 실제값 in zip(기대값들, 실제값들):
    if 기대값 != 실제값:
        print(f"불일치 발견! {기대값} vs {실제값}")


# list comprehension
# 리스트를 순회하면서 조건에따라 데이터를 가공해 주는겁니다. (for + if + append)
numbers = [1, 2, 3, 4, 5]
result = [x * 2 for x in numbers if x % 2 == 0]
print(result)

명단 = [
    {
        "이름": "김철수",
        "나이": 20,
    },
    {
        "이름": "박철수",
        "나이": 15,
    },
    {
        "이름": "이철수",
        "나이": 36,
    },
    {
        "이름": "최철수",
        "나이": 12,
    },
    {
        "이름": "강철수",
        "나이": 33,
    },
]
고객출석표 = [
    고객정보["이름"] + "님"
    for 고객정보 in 명단
    if not 고객정보["이름"].startswith("김")
]
print(고객출석표)
고객출석표 = []
for 고객정보 in 명단:
    if 고객정보["이름"].startswith("김"):
        continue
    고객출석표.append(고객정보["이름"] + "님")
print(고객출석표)

# 길이 구하기
response = [[1, 2, 3, 4], [5, 6, 7], [5, 5, 767, 2, 3, 57], [123, 67, 35]]
len_of_response = [len(list) for list in response]
print(len_of_response)

# 평탄화작업
flat_response = [num for list in response for num in list]
print(flat_response)

sorted(명단, key=lambda 고객정보: 고객정보["나이"])
print(명단)
