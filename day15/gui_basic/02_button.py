from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("400x600")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=10, pady=5, text="버튼2")  # 숫자: 픽셀(px)단위
btn2.pack()

btn3 = Button(root, width=10, height=5, text="버튼3")
# width=10:글자 10개 들어갈 크기
# height=5: 글자 5줄 들어갈 크기
btn3.pack()

root.mainloop()
