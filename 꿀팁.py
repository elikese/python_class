# 튜플 언패킹
홍길동씨 = ("홍길동", "조선", 30, "남자", True)
이름, 국적, 나이, 성별, 결혼여부 = 홍길동씨
print(이름)
print(국적)
print(나이)
print(성별)
print(결혼여부)

# 리스트 언패킹
기차 = ["1호칸", "2호칸", "3호칸", "4호칸", "5호칸"]
맨앞칸, *중간칸들, 맨뒷칸 = 기차
print(f"맨앞칸={맨앞칸}, 중간칸들={중간칸들}, 맨뒷칸={맨뒷칸}")

# any , all
any([False, False, True])  # 하나라도 True면, True
all([True, True, False])  # 하나라도 False면, False
