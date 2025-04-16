# 딕셔너리
김철수씨 = {
    "이름": "김철수",
    "나이": 30,
    "국적": "대한민국",
    "성별": "남자",
    "취미": ["코딩", "독서", "음악감상"],
}

박철수씨 = dict(
    이름="박철수",
    나이=30,
    국적="대한민국",
    성별="남자",
    취미=["축구", "유투브보기", "야구"],
)

# { 키(key) : 값(value) } 의 형태로 이루어져 있음
# key는 중복, 수정 안됨.

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

# dict 요소 삭제
김철수씨.pop("이름")
print(김철수씨)

# 관련함수들
