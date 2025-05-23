from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

label1 = Label(root, text="hello", font=("Arial", 20), bg="white", fg="black")
label1.pack()

label_config1 = {
    "text": "hello",
    "font": ("Arial", 20),
    "bg": "white",
    "fg": "black",
}

label_config2 = {
    "text": "world",
    "font": ("Arial", 20),
    "bg": "black",
    "fg": "white",
}

label_status = {"status": "config1"}


def change():
    if label_status.get("status") == "config1":
        label1.config(**label_config2)
        label_status["status"] = "config2"
    elif label_status.get("status") == "config2":
        label1.config(**label_config1)
        label_status["status"] = "config1"


btn = Button(root, text="클릭!", command=change)
btn.pack()

img1 = PhotoImage(file="img1.png")
label2 = Label(root, image=img1)
label2.pack()

root.mainloop()
