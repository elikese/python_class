from tkinter import *

root = Tk()
root.geometry("320x320")
root.title("버튼 연습")

"""
1. 불러오기 버튼
    불러오기 버튼을 누르면 listbox에서 선택한 것을 왼쪽 ui에 내용을 보여 줌
    curselection 이 없으면 msgbox.showwarning 호출하고 바로 리턴

2. 수정 버튼
    평소에는 누르지못하게 비활성화
    불러오기 버튼으로 showwarning에 안걸리면 활성화
    수정버튼을 누르면 기존 index에 덮어쓰기

3. 저장 버튼
    평소에는 활성화 되어있다가
    불러오기 버튼으로 showwarning에 안걸리면 비활성화
    
    수정버튼이 활성화 -> 저장버튼은 비활성화
    수정버튼이 비활성화 -> 저장버튼은 활성화
"""


# 저장클릭 -> 수정활성, 저장비활성
# 수정클릭 -> 저장활성, 수정비활성


# 실습) click_update
def click_update():
    # 저장버튼 활성화
    # 수정버튼은 비활성화
    update_btn.config(state="disabled")
    save_btn.config(state="normal")


# tkinter 위젯 -> 속성들은 key-value 쌍으로 관리
# key로 value를 확인할 수 있다
def click_save():
    # cget - configure_get
    print(save_btn.cget("width"))
    print(save_btn.cget("text"))
    print(save_btn.cget("state"))
    print(save_btn["state"])
    # __getitem__(key): -> return self.cget(key)

    update_btn.config(state="normal")
    save_btn.config(state="disabled")


update_btn = Button(root, text="수정", width=30, command=click_update, state="disabled")
update_btn.pack(pady=5)
save_btn = Button(root, text="저장", width=30, command=click_save)
save_btn.pack(pady=5)


root.mainloop()
