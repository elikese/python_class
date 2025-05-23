from tkinter import *

# 똑같은 것이 계속 반복
# 1. 스타일이 사실상 고정인데, text만 바뀌고 있다.
#       -> text만 주입하고, 나머지는 고정값을 쓰고 싶어요.
#       -> Button을 상속받아서 해결
# 2. grid로 쌓아가는 방식도 규칙적
#       -> 2차원 list만들어서 (list 안에 list)
#       -> 2중 for문으로 상속받은 Button 생성
# 3. grid도 지금 주입받는게 row, col, rowspan 말고 다 동일
#       -> 상속받았으니까, 오버라이드

root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

button_frame = Frame(root)
button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


class CustomButton(Button):
    def __init__(self, parent, text, **kwargs):
        super().__init__(parent, text=text, width=8, height=5, **kwargs)

    def grid(self, **options):
        my_options = {"sticky": "nsew", "padx": 3, "pady": 3}
        my_options.update(options)
        super().grid(**my_options)


button_layout = [
    ["clear", "/", "*", "-"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", "enter"],
    ["1", "2", "3", "enter"],
]

for 줄idx, 줄 in enumerate(button_layout):
    for 요소idx, 요소 in enumerate(줄):
        if 요소 != "enter":
            CustomButton(button_frame, text=요소).grid(row=줄idx, column=요소idx)

CustomButton(button_frame, text="enter").grid(row=2, column=3, rowspan=2)

root.mainloop()
