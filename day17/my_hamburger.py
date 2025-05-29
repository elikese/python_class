from tkinter import *
import tkinter.ttk as ttk

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
hamburger_quantity = IntVar()


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
    pass


title_label = Label(root, text="🍔햄버거 주문🍔", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

hamburger_frame = Frame(root, width=320, height=320)
hamburger_frame.propagate(False)
hamburger_frame.pack(pady=10)

# cheese = Radiobutton(hamburger_frame, text="치즈버거", value="치즈버거", variable=selected_hamburger)
# cheese.grid(row=0, column=0, sticky="w")
# cheese_price_label = Label(hamburger_frame, text="3000원")
# cheese_price_label.grid(row=0, column=1, sticky="e")
#
# bulgogi = Radiobutton(hamburger_frame, text="불고기버거", value="불고기버거", variable=selected_hamburger)
# bulgogi.grid(row=1, column=0, sticky="w")
# bulgogi_price_label = Label(hamburger_frame, text="3500원")
# bulgogi_price_label.grid(row=1, column=1, sticky="e")

# 반복 -> 반복문을 써야한다.
# 어떤게 반복되는지 찾아야 함

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
cart = Listbox(root, width=30, height=8, selectmode=SINGLE)
cart.pack(pady=6)

Button(root, text="선택 삭제", width=30, command=delete_click).pack(pady=5)
Button(root, text="주문 하기", width=30, command=order_click).pack(pady=5)
root.mainloop()
