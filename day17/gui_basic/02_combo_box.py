import tkinter.ttk as ttk
from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

combo_values = ["월", "화", "수", "목", "금"]
combo_box1 = ttk.Combobox(root, height=5, values=combo_values)
combo_box1.set("요일 선택")
combo_box1.pack()

combo_box2 = ttk.Combobox(root, height=5, values=combo_values, state="readonly")
combo_box2.current(0)
combo_box2.pack()


def click():
    print(combo_box1.get())  # 선택값 리턴
    print(combo_box2.get())


btn1 = Button(root, text="선택", command=click)
btn1.pack()

root.mainloop()
