import tkinter as tk
from tkinter import messagebox
import datetime

# 전역 변수
order_list = {}  # 주문 내역을 저장할 딕셔너리
total_price = 0  # 총 가격

# 메뉴 데이터
food_menu = {"김치찌개": 8000, "된장찌개": 7000, "불고기": 15000, "비빔밥": 9000}
drink_menu = {"콜라": 2000, "사이다": 2000, "커피": 3000, "물": 1000}


# 메뉴 추가 함수
def add_menu(menu_name, price):
    if menu_name in order_list:
        order_list[menu_name] += 1  # 이미 있으면 수량 +1
    else:
        order_list[menu_name] = 1  # 없으면 새로 추가

    update_order_display()  # 주문 내역 화면 업데이트


# 주문 내역 화면 업데이트 함수
def update_order_display():
    global total_price

    # 기존 내용 삭제
    order_text.delete(1.0, tk.END)

    total_price = 0
    order_info = "=== 주문 내역 ===\n"

    for menu_name, quantity in order_list.items():
        # 가격 찾기
        if menu_name in food_menu:
            price = food_menu[menu_name]
        else:
            price = drink_menu[menu_name]

        subtotal = price * quantity
        total_price += subtotal

        order_info += f"{menu_name}: {quantity}개 - {subtotal:,}원\n"

    order_info += f"\n총 가격: {total_price:,}원"
    order_text.insert(tk.END, order_info)


# 전체 삭제 함수
def clear_all():
    global order_list
    order_list = {}
    update_order_display()


# 주문하기 함수
def place_order():
    if not order_list:
        messagebox.showwarning("알림", "주문할 메뉴가 없습니다!")
        return

    # 주문 확인 메시지 만들기
    order_summary = "주문 내역:\n"
    for menu_name, quantity in order_list.items():
        if menu_name in food_menu:
            price = food_menu[menu_name]
        else:
            price = drink_menu[menu_name]

        subtotal = price * quantity
        order_summary += f"{menu_name}: {quantity}개 - {subtotal:,}원\n"

    order_summary += f"\n총 가격: {total_price:,}원\n\n주문하시겠습니까?"

    # 확인 메시지박스
    result = messagebox.askyesno("주문 확인", order_summary)

    if result:  # 예를 눌렀을 때
        save_log()  # 로그 저장
        messagebox.showinfo("완료", "주문이 완료되었습니다!")
        clear_all()  # 주문 내역 초기화


# 로그 저장 함수
def save_log():
    now = datetime.datetime.now()
    filename = f"주문_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"주문 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 30 + "\n")

        for menu_name, quantity in order_list.items():
            if menu_name in food_menu:
                price = food_menu[menu_name]
            else:
                price = drink_menu[menu_name]

            subtotal = price * quantity
            f.write(f"{menu_name}: {quantity}개 - {subtotal:,}원\n")

        f.write("=" * 30 + "\n")
        f.write(f"총 가격: {total_price:,}원\n")


# 메인 윈도우 생성
window = tk.Tk()
window.title("음식 주문")
window.geometry("800x600")

# 제목
title_label = tk.Label(window, text="음식점 주문 키오스크", font=("Arial", 20))
title_label.pack(pady=10)

# 메인 프레임 (왼쪽: 메뉴, 오른쪽: 주문내역)
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10)

# 왼쪽 프레임 - 메뉴
menu_frame = tk.Frame(main_frame)
menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

# 음식 메뉴 제목
food_title = tk.Label(menu_frame, text="음식 메뉴", font=("Arial", 14, "bold"))
food_title.pack(pady=5)

# 음식 메뉴 버튼들
for menu_name, price in food_menu.items():
    btn_text = f"{menu_name} - {price:,}원"
    btn = tk.Button(
        menu_frame,
        text=btn_text,
        width=20,
        height=2,
        command=lambda name=menu_name, p=price: add_menu(name, p),
    )
    btn.pack(pady=2)

# 음료 메뉴 제목
drink_title = tk.Label(menu_frame, text="음료 메뉴", font=("Arial", 14, "bold"))
drink_title.pack(pady=(20, 5))

# 음료 메뉴 버튼들
for menu_name, price in drink_menu.items():
    btn_text = f"{menu_name} - {price:,}원"
    btn = tk.Button(
        menu_frame,
        text=btn_text,
        width=20,
        height=2,
        command=lambda name=menu_name, p=price: add_menu(name, p),
    )
    btn.pack(pady=2)

# 오른쪽 프레임 - 주문 내역
order_frame = tk.Frame(main_frame)
order_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=5)

# 주문 내역 제목
order_title = tk.Label(order_frame, text="주문 내역", font=("Arial", 14, "bold"))
order_title.pack(pady=5)

# 주문 내역 텍스트 박스
order_text = tk.Text(order_frame, width=25, height=20)
order_text.pack(pady=5)

# 전체 삭제 버튼
clear_btn = tk.Button(
    order_frame, text="전체 삭제", bg="red", fg="white", command=clear_all
)
clear_btn.pack(pady=5)

# 주문하기 버튼 (하단)
order_btn = tk.Button(
    window,
    text="주문하기",
    font=("Arial", 16, "bold"),
    bg="orange",
    fg="white",
    height=2,
    command=place_order,
)
order_btn.pack(fill=tk.X, padx=10, pady=10)

# 프로그램 시작
window.mainloop()
