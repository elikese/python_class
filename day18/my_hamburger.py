from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os

root = Tk()
root.geometry("320x640")
root.title("햄버거")

# 메뉴 데이터(전역)
hamburgers = {"치즈버거": 3000, "불고기버거": 3500, "치킨버거": 4000, "새우버거": 3600}
drinks = {"콜라": 1500, "사이다": 1500, "제로콜라": 1700}
cart_data = {}

selected_hamburger = StringVar()
selected_hamburger.set(None)
selected_drink = StringVar()
selected_drink.set(None)


###################################################################################
# 함수
def burger_click():
    burger_name = selected_hamburger.get()
    if not burger_name or burger_name == "None":
        return

    price = hamburgers.get(burger_name)
    # cart.insert(END, f"{burger_name} - {price}원")
    # 갯수만 늘어나게 바꿔야함

    # 총 갯수를 구해줘야 함
    # dict - key, value
    # value자리에 또 dict가 올 수 있음
    if burger_name in cart_data:
        cart_data[burger_name]["quantity"] += 1
    else:
        cart_data[burger_name] = {"price": price, "quantity": 1}
    refresh_cart_view()


def drink_click():
    drink_name = selected_drink.get()
    if not drink_name or drink_name == "None":
        return

    price = drinks.get(drink_name)
    if drink_name in cart_data:
        cart_data[drink_name]["quantity"] += 1
    else:
        cart_data[drink_name] = {"price": price, "quantity": 1}
    refresh_cart_view()


def refresh_cart_view():
    cart.delete(0, END)
    for name, data in cart_data.items():
        total_price = data["price"] * data["quantity"]
        cart.insert(END, f"{name} - {data['quantity']}개 - {total_price}원")


def delete_click():
    index_tuple = cart.curselection()
    if not index_tuple:
        return

    index = index_tuple[0]
    selected_text = cart.get(index).strip()  # "~버거 - ~개 - ~원"
    item_name = selected_text.split(" - ")[0]  # "~버거"

    # 삭제
    cart_data.pop(item_name)
    refresh_cart_view()


def order_click():
    if not cart_data:
        messagebox.showwarning("주문 확인", "장바구니가 비어있습니다!")
        return

    # 주문 내역 문자열 만들기
    order_text = "주문 내역\n"
    total_amount = 0

    for name, data in cart_data.items():
        item_total = data["price"] * data["quantity"]
        total_amount += item_total
        order_text += f"{name} - {data['quantity']}개 - {item_total}원\n"

    order_text += f"\n총 금액: {total_amount}원"

    # 주문 확인 메시지박스
    result = messagebox.askyesno("주문 확인", order_text + "\n주문하시겠습니까?")

    if result:  # 예를 눌렀을 때
        save_order_log(order_text, total_amount)
        cart_data.clear()  # 장바구니 비우기
        refresh_cart_view()  # 화면 업데이트
        messagebox.showinfo("주문 완료", "주문이 완료되었습니다!")


def save_order_log(order_text, total_amount):
    """주문 내역을 텍스트 파일로 저장"""
    try:
        # 현재 날짜와 시간 가져오기
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # 로그 파일명 (order_log.txt)
        log_filename = "order_log.txt"

        # 주문 로그 내용 작성
        log_content = f"""\
{'='*50}
주문 시간: {timestamp}
{'='*50}
{order_text}
총 금액: {total_amount}원
{'='*50}
"""

        # 파일에 추가 모드로 저장 (기존 로그 유지)
        with open(log_filename, "a", encoding="utf-8") as f:
            f.write(log_content)

        print(f"주문 로그가 {log_filename}에 저장되었습니다.")

    except Exception as e:
        print(f"로그 저장 중 오류 발생: {e}")
        messagebox.showerror("오류", f"로그 저장 실패: {e}")


###################################################################################

title_label = Label(root, text="🍔햄버거 주문🍔", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

hamburger_frame = Frame(root, width=320, height=320)
hamburger_frame.propagate(False)
hamburger_frame.pack(pady=10)

for idx, (burger_name, price) in enumerate(hamburgers.items()):
    Radiobutton(hamburger_frame, text=burger_name, value=burger_name, variable=selected_hamburger).grid(row=idx, column=0, sticky="w")
    Label(hamburger_frame, text=f"{price}원").grid(row=idx, column=1, sticky="e")

Button(hamburger_frame, text="담기", width=30, command=burger_click).grid(row=len(hamburgers), column=0, columnspan=2, pady=5)

drink_frame = Frame(root, width=320, height=320)
drink_frame.propagate(False)
drink_frame.pack(pady=10)

for idx, (drink_name, price) in enumerate(drinks.items()):
    Radiobutton(drink_frame, text=drink_name, value=drink_name, variable=selected_drink).grid(row=idx, column=0, sticky="w")
    Label(drink_frame, text=f"{price}원").grid(row=idx, column=1, sticky="e")

Button(drink_frame, text="담기", width=30, command=drink_click).grid(row=len(drinks), column=0, columnspan=2, pady=5)

cart_label = Label(root, text="장바구니", font=("Arial", 18, "bold"))
cart_label.pack(pady=5)
cart = Listbox(root, width=30, height=8, selectmode=SINGLE, font=("Courier New", 10))
cart.pack(pady=6)

Button(root, text="선택 삭제", width=30, command=delete_click).pack(pady=5)
Button(root, text="주문 하기", width=30, command=order_click).pack(pady=5)
root.mainloop()
