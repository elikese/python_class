from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

label1 = Label(root, text="메뉴를 선택하세요")
label1.pack()

radio_variable1 = IntVar()
# radio_button1 = Radiobutton(root, text="햄버거", value=0, variable=radio_variable1)
# radio_button2 = Radiobutton(root, text="피자", value=1, variable=radio_variable1)
# radio_button3 = Radiobutton(root, text="치킨", value=2, variable=radio_variable1)
# radio_button1.pack()
# radio_button2.pack()
# radio_button3.pack()

food_menu_options = [
    {"text": "햄버거", "value": 0, "variable": radio_variable1},
    {"text": "피자", "value": 1, "variable": radio_variable1},
    {"text": "치킨", "value": 2, "variable": radio_variable1},
]
for food_option in food_menu_options:
    Radiobutton(root, **food_option).pack()


label1 = Label(root, text="음료를 선택하세요")
label1.pack()

radio_variable2 = IntVar()  # variable을 공유 -> 하나의 상태로 관리되어짐
radio_button4 = Radiobutton(root, text="콜라", value=0, variable=radio_variable2)
radio_button5 = Radiobutton(root, text="사이다", value=1, variable=radio_variable2)
radio_button6 = Radiobutton(root, text="맥주", value=2, variable=radio_variable2)

radio_button4.pack()
radio_button5.pack()
radio_button6.pack()


def click():
    print("----------------")
    print(radio_variable1.get())
    print(radio_variable2.get())
    pass


btn1 = Button(root, text="주문", command=click)
btn1.pack()

root.mainloop()
