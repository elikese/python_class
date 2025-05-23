from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

check_variable1 = IntVar()
# check_box1의 상태를 int형으로 check_variable이라는 변수에 저장
# 체크: 1, 체크 해제: 0
check_box1 = Checkbutton(root, text="hello", variable=check_variable1)
check_box1.select()  # 선택 처리
check_box1.deselect()  # 선택 해제 처리
check_box1.pack()

check_variable2 = IntVar()
check_box2 = Checkbutton(root, text="world", variable=check_variable2)
check_box2.pack()


def click():
    print(check_variable1.get())
    print(check_variable2.get())
    pass


btn1 = Button(root, text="클릭", command=click)
btn1.pack()


root.mainloop()
