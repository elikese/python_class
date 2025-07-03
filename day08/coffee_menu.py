"""
커피집 할인 이벤트
월요일 : 10퍼 할인
화/수/목/금요일: 5퍼 할인
토/일: 15퍼 할인
"""


# 할인율 계산 함수
def week_discount_calc(day):
    day = day.strip()  # 앞뒤 공백 제거
    day = day.replace("요일", "")  # '요일' 제거

    if day == "월":
        return 0.9
    elif day in ["화", "수", "목", "금"]:
        return 0.95
    elif day in ["토", "일"]:
        return 0.85
    else:
        return 1


# 메뉴판
menu = {1: ("아메리카노", 4000), 2: ("카푸치노", 4500), 3: ("바닐라라떼", 5000)}

# 사용자 입력
menu_choice = int(input("메뉴를 선택하세요 (1.아메리카노 2.카푸치노 3.바닐라라떼): "))
day_input = input("오늘은 무슨 요일인가요?")

# 데이터 가져오기
menu_name, price = menu.get(menu_choice)  # 튜플 언패킹

# 할인율 계산
discount_rate = week_discount_calc(day_input)
final_price = int(price * discount_rate)

print(
    f"""
[주문내역]
메뉴: {menu_name}
요일: {day_input}
원가: {price}
할인 적용 가격: {final_price}원
""".strip()
)
