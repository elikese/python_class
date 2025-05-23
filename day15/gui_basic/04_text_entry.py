from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

txt = Text(root, width=30, height=5)
txt.insert(END, "여러줄 입력")
txt.pack()

entry = Entry(root, width=30)  # 한줄 입력(개행 없음)
entry.insert(0, "한줄입력")  # 문자열처럼 생각(0번째부터)
entry.pack()


def click():
    print(txt.get("1.0", END).strip())  # 1: 첫번째라인, 0:문자열 0번째부터
    print(entry.get())

    # 내용 삭제
    txt.delete("1.0", END)
    entry.delete(0, END)


btn = Button(root, text="클릭", command=click)
btn.pack()

root.mainloop()
