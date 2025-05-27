# 복습
from tkinter import *

root = Tk()  # 새로운 창 생성
root.geometry("320x320")  # 창 크기 설정
root.title("연습")  # 창 이름 설정
root.resizable(False, False)  # 사이즈 조절여부 설정


title_label = Label(root, text="제목", font=("Arial", 18, "bold"))  # 글자표기
title_label.pack(pady=5)
title_entry = Entry(root, width=30)  # 한줄 입력
title_entry.pack(pady=5)
# title_entry.get() # 전체 문자열 가져옴
# title_entry.delete(0, END) # 전체삭제

content_label = Label(root, text="아래에 내용을 입력하세요")  # 글자표기
content_label.pack(pady=5)
content_text = Text(root, width=30, height=8)
content_text.pack(pady=5)
# content_text.get("1.0", END) # 전체 문자열 가져옴
# content_text.delete("1.0", END) # 전체삭제


def button_click():
    # 버튼을 클릭했을때, "제목: {}, 내용: {}" 콘솔창에 출력!
    title = title_entry.get()
    content = content_text.get("1.0", END).strip()
    # Text는 줄 단위로 관리되기 때문에 항상 마지막에 개행(\n)이 붙어 있음
    print(f"제목: {title}, 내용: {content}")
    pass


# 1. 쓴 글을 dict로 포장해서 JSON으로 만든 후 저장
# 2. 쓴 글을 class화해서 JSON으로 만든 후 저장
import json
import os


def load_writing_json():
    with open("./writing.json", "r", encoding="utf-8") as f:
        return json.load(f)


def save_click():
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


button = Button(root, text="확인", width=30, command=button_click)  # 버튼 생성
# command -> 클릭됬을 때 호출할 함수
button.pack(pady=5)

save_button = Button(root, text="저장", width=30, command=save_click)
save_button.pack(pady=5)

root.mainloop()  # 실행
