# 복습
from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()  # 새로운 창 생성
root.geometry("640x320")  # 창 크기 설정
root.title("연습")  # 창 이름 설정
# root.resizable(False, False)  # 사이즈 조절여부 설정

###########################################################################
# frame은 가상의 공간
# 두개의 같은 size frame을 만들어서
# 하나는 왼쪽, 하나는 오른쪽
left_frame = Frame(root, width=320, height=320)
left_frame.propagate(False)  # 위젯의 크기에 줄어들지 못하게 방지
left_frame.pack(side=LEFT)

right_frame = Frame(root, width=320, height=320)
right_frame.propagate(False)
right_frame.pack(side=LEFT)
###########################################################################

title_label = Label(left_frame, text="제목", font=("Arial", 18, "bold"))  # 글자표기
title_label.pack(pady=5)
title_entry = Entry(left_frame, width=30)  # 한줄 입력
title_entry.pack(pady=5)
# title_entry.get() # 전체 문자열 가져옴
# title_entry.delete(0, END) # 전체삭제

content_label = Label(left_frame, text="아래에 내용을 입력하세요")  # 글자표기
content_label.pack(pady=5)
content_text = Text(left_frame, width=30, height=8)
content_text.pack(pady=5)
# content_text.get("1.0", END) # 전체 문자열 가져옴
# content_text.delete("1.0", END) # 전체삭제

###########################################################################
listbox_label = Label(right_frame, text="글 목록", font=("Arial", 18, "bold"))
listbox_label.pack(pady=5)
listbox = Listbox(right_frame, width=30, height=10, selectmode=SINGLE)
listbox.pack(pady=6)


def print_listbox():
    if not os.path.exists("./writing.json"):
        return  # 파일이 없으면 아무 것도 안 함

    listbox.delete(0, END)  # 싹 다 지우고
    writing_list = load_writing_json()
    for dict_data in writing_list:
        listbox.insert(END, dict_data.get("title"))


def button_click():
    # 버튼을 클릭했을때, "제목: {}, 내용: {}" 콘솔창에 출력!
    title = title_entry.get()
    content = content_text.get("1.0", END).strip()
    # Text는 줄 단위로 관리되기 때문에 항상 마지막에 개행(\n)이 붙어 있음
    print(f"제목: {title}, 내용: {content}")


# 1. 쓴 글을 dict로 포장해서 JSON으로 만든 후 저장
# 2. 쓴 글을 class화해서 JSON으로 만든 후 저장
import json
import os


def load_writing_json():
    with open("./writing.json", "r", encoding="utf-8") as f:
        return json.load(f)


def save_click():
    ###########################################################################
    response = msgbox.askokcancel("저장", "저장 하시겠습니까?")
    ###########################################################################
    if response:
        # 해당 경로에 있는지 없는지 검사
        # 없다면 빈 리스트 JSON file 생성
        if not os.path.exists("./writing.json"):
            with open("./writing.json", "w", encoding="utf-8") as f:
                json.dump([], f)

        writing_list = load_writing_json()

        with open("./writing.json", "w", encoding="utf-8") as f:
            title = title_entry.get()
            content = content_text.get("1.0", END).strip()
            dict_date = {
                "title": title,
                "content": content,
            }
            writing_list.append(dict_date)
            json.dump(writing_list, f, ensure_ascii=False, indent=4)

        title_entry.delete(0, END)
        content_text.delete("1.0", END)
        print_listbox()


# 1. listbox에서 선택된 index 리턴받기
# 2. file에 있는 list 가져와서 해당 index 삭제
# 3. 다시 JSON으로 write


# 실습) askyescancel msgbox로
# "{title} 삭제하시겠습니까?"
# 예를 선택할때 삭제되게
def delete_click():
    index_tuple = listbox.curselection()  # index 리턴 -> (0,) 튜플 형태
    if not index_tuple:  # 선택한게 없으면, 빠른리턴
        return

    response = msgbox.askokcancel("삭제", f"{listbox.get(index_tuple[0])} 삭제하시겠습니까?")
    if response:
        writing_list = load_writing_json()  # file 불러오기
        data = writing_list.pop(index_tuple[0])  # 해당 index 삭제

        with open("./writing.json", "w", encoding="utf-8") as f:
            json.dump(writing_list, f, ensure_ascii=False, indent=4)

        print_listbox()


def load_click():
    index_tuple = listbox.curselection()
    if not index_tuple:
        msgbox.showwarning("경고", "목록에서 항목을 선택하세요.")
        return

    index = index_tuple[0]
    writing_list = load_writing_json()

    selected_data = writing_list[index]

    title_entry.delete(0, END)
    content_text.delete("1.0", END)

    title_entry.insert(0, selected_data["title"])
    content_text.insert("1.0", selected_data["content"])


button = Button(left_frame, text="확인", width=30, command=button_click)  # 버튼 생성
# command -> 클릭됬을 때 호출할 함수
button.pack(pady=5)

save_button = Button(left_frame, text="저장", width=30, command=save_click)
save_button.pack(pady=5)

update_button = Button(right_frame, text="선택 불러오기", width=30, command=load_click)
update_button.pack(pady=5)

delete_button = Button(right_frame, text="선택 삭제", width=30, command=delete_click)
delete_button.pack(pady=5)


print_listbox()
root.mainloop()  # 실행
