# 딕셔너리(dict) { }
# 리스트와 튜플은 순서(숫자)로 요소에 접근! 0번 인덱스,1번 인덱스,2번 인덱스... -> 데이터를 숫자로 관리
# 딕셔너리는 key를 통해 요소에 접근! -> 데이터에 라벨을 붙혀서 관리
# key: 불변하는 자료형이면 key로 사용가능!

김철수씨 = {
    "이름": "김철수",
    "나이": 30,
    "국적": "대한민국",
    "성별": "남자",
    "취미": ["코딩", "독서", "음악감상"],
}

김철수씨 = dict(
    이름="김철수",
    나이=30,
    국적="대한민국",
    성별="남자",
    취미=["코딩", "독서", "음악감상"],
)

# { 키(key) : 값(value) } 의 형태로 이루어져 있음
# key는 중복 안됨.

# dict 요소 접근
print(김철수씨["국적"])  # key가 없으면, 에러발생
print(김철수씨.get("국적"))  # key가 없으면, None을 반환

# dict 요소 추가, 수정
김철수씨["결혼유무"] = False  # 없었던 key에 value를 할당하면 추가
김철수씨["나이"] = 31  # 기존 있었던 key에 value를 할당하면 수정
print(김철수씨)

김철수씨.update(
    {"이름": "김철목", "나이": 31, "취미": ["코딩", "독서", "음악감상", "유투브보기"]}
)  # 기존 있었던 key는 수정되고, 없었던 key들은 추가된다
print(김철수씨)

# dict 요소 삭제 : pop()
# dict에서는 pop()에 key를 넣어줌. pop(key)로 꺼내온건 key에 해당하는 value
김철수씨.pop("이름")
print(김철수씨)

# len , in 연산자 -> key를 기준으로 작동
print(len(김철수씨))
print("이름" in 김철수씨)

# keys(), values(), items() -> 일반적으로 반복문과 함께 사용 -> 반복문 배울때 또 복습
전화번호부 = {
    "김철수": "010-1111-1111",
    "박철수": "010-2222-2222",
    "이철수": "010-3333-3333",
}
# keys(): key들만 모아준다.
이름들 = 전화번호부.keys()
print(이름들)
print(type(이름들))  # 리스트는 아니다!(읽기전용 자료형)
print(list(이름들))  # 리스트로 형변환해서 사용가능

# values(): value들만 모아준다
전화번호들 = 전화번호부.values()
print(list(전화번호부))

# items(): (키, 값) 쌍을 튜플로 묶어 모아준다
전화번호부_튜플들 = 전화번호부.items()
print(list(전화번호부_튜플들))

# 실습) 음식 메뉴판
메뉴판 = {"김밥": 3000, "라면": 4000, "돈까스": 7000}
# 1. 메뉴판에 떡복이(5000)원을 추가하세요
# 2. 라면가격을 5000원으로 올려주세요
# 3. 철수는 김밥과 라면을 먹었는데, 철수가 내야할 금액을 dict로 접근해서 계산하여 출력해주세요
# 철수_내야할돈 = dict[] + dict[]
메뉴판.update({"라면": 5000, "떡볶이": 5000})
print(메뉴판)
철수_내야할돈 = 메뉴판["김밥"] + 메뉴판["라면"]
print(철수_내야할돈)

# 실습2) 맛집데이터
# 맛집데이터는 좌표 튜플을 key로, value에는 맛집이름이 저장되어 있다.
# 입맛이 까다로운 철수는 길을 가다가 (15, 30)에서 한식집을 찾았는데, 이집이 맛집인지 확인하려한다
# 1. if문 + in 연산자 사용하여, 맛집인지 아닌지 확인한다.
# 2. 맛집이라면 맛집이름이 무엇인지 출력하시오
맛집데이터 = {
    (5, 10): "에드워드리 가게",
    (10, 20): "최현석 가게",
    (15, 30): "급식대가 가게",
    (20, 40): "나폴리 맛피아 가게",
    (25, 50): "철가방요리사 가게",
}

if (15, 30) in 맛집데이터:
    print(맛집데이터[(15, 30)])
else:
    print("맛집이 아니야. 난 먹지 않겠어")

# key로 튜플이 사용가능하다
# dict의 key는 불변형만 사용가능하다
# 튜플은 불변형이라서 key로 사용될 수 있었구나
