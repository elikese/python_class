import tkinter.messagebox as msgbox
from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)


def info():
    msgbox.showinfo("정상", "정상입니다")


def warning():
    msgbox.showwarning("경고", "경고입니다")


def error():
    msgbox.showerror("에러", "에러입니다")


def okcancel():
    response = msgbox.askokcancel("선택해주세요", "선택해주십시오")
    print(response)


def yesnocancel():
    response = msgbox.askyesnocancel(title="예,아니오,취소", message="예, 아니오, 취소")
    print(response)


Button(root, text="정상알림", command=info).pack()
Button(root, text="경고알림", command=warning).pack()
Button(root, text="에러알림", command=error).pack()
Button(root, text="선택알림", command=okcancel).pack()
Button(root, text="예 아니오 취소", command=yesnocancel).pack()

root.mainloop()
