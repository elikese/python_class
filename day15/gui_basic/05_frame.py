from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

frame1 = Frame(root, width=150, height=100, bg="skyblue")
frame1.pack()
frame1.pack_propagate(False)
# frame은 랩핑처럼 자동으로 안에 있는 위젯크기에 맞춰짐
# 안에 있는 위젯이 너무 작으면, width, height이 무시됨
# 그걸 방지하는 메서드입니다

Button(frame1, text="버튼1").pack()
Button(frame1, text="버튼2").pack()
Button(frame1, text="버튼3").pack()

label_frame = LabelFrame(root, text="음료", width=150, height=100, bg="lightgreen")
label_frame.pack()
label_frame.pack_propagate(False)
Button(label_frame, text="콜라").pack()
Button(label_frame, text="사이다").pack()

root.mainloop()
