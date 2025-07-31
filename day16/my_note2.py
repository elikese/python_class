from tkinter import *
import tkinter.messagebox as msgbox  # 알림창 사용
import json
import os

root = Tk()
root.geometry("640x320")  # 1. 화면을 넓혀서 왼쪽/오른쪽 구분
root.title("연습")

# 2. Frame으로 화면을 왼쪽/오른쪽으로 나누기 - 입력부와 목록부 분리
left_frame = Frame(root, width=320, height=320)
left_frame.propagate(False)  # 3. 자동 크기 조절 방지
left_frame.pack(side=LEFT)

right_frame = Frame(root, width=320, height=320)
right_frame.propagate(False)
right_frame.pack(side=LEFT)

# 4. 왼쪽 프레임: 입력 부분
title_label = Label(left_frame, text="제목", font=("Arial", 18, "bold"))
title_label.pack(pady=5)
title_entry = Entry(left_frame, width=30)
title_entry.pack(pady=5)

content_label = Label(left_frame, text="아래에 내용을 입력하세요")
content_label.pack(pady=5)
content_text = Text(left_frame, width=30, height=8)
content_text.pack(pady=5)

# 5. 오른쪽 프레임: 글 목록 부분
listbox_label = Label(right_frame, text="글 목록", font=("Arial", 18, "bold"))
listbox_label.pack(pady=5)
listbox = Listbox(right_frame, width=30, height=10, selectmode=SINGLE)
listbox.pack(pady=5)

# 6. 현재 수정 중인 글의 인덱스 저장 - 새 글인지 수정인지 구분
current_editing_index = None


def load_writing_json():
    with open("./writing.json", "r", encoding="utf-8") as f:
        return json.load(f)


# 7. 리스트박스에 저장된 글 제목들 표시하는 함수
def print_listbox():
    if not os.path.exists("./writing.json"):
        return

    listbox.delete(0, END)  # 8. 기존 목록 모두 삭제
    writing_list = load_writing_json()
    for dict_data in writing_list:
        listbox.insert(END, dict_data.get("title"))  # 9. 제목만 리스트박스에 추가


# 10. UI 상태 업데이트 - 수정모드/새글모드에 따라 버튼 텍스트 변경
def update_ui_state():
    global current_editing_index
    if current_editing_index is not None:
        save_button.config(text="수정")  # 11. 수정 모드일 때
        load_button.config(state=DISABLED)  # 12. 다른 글 불러오기 비활성화
        delete_button.config(state=DISABLED)
    else:
        save_button.config(text="저장")  # 13. 새 글 모드일 때
        load_button.config(state=NORMAL)
        delete_button.config(state=NORMAL)


# 14. 저장/수정 기능이 통합된 함수
def save_click():
    global current_editing_index

    title = title_entry.get()
    content = content_text.get("1.0", END).strip()

    # 15. 빈 값 체크 - 사용자가 실수로 빈 글 저장하는 것 방지
    if not title or not content:
        msgbox.showwarning("경고", "제목과 내용을 모두 입력해주세요.")
        return

    if current_editing_index is not None:
        # 16. 수정 모드 - 기존 글을 업데이트
        response = msgbox.askokcancel("수정", f"'{title}' 글을 수정하시겠습니까?")
        if response:
            writing_list = load_writing_json()
            writing_list[current_editing_index] = {
                "title": title,
                "content": content,
            }

            with open("./writing.json", "w", encoding="utf-8") as f:
                json.dump(writing_list, f, ensure_ascii=False, indent=4)

            # 17. 수정 완료 후 상태 초기화
            current_editing_index = None
            title_entry.delete(0, END)
            content_text.delete("1.0", END)
            print_listbox()
            update_ui_state()
            msgbox.showinfo("완료", "수정이 완료되었습니다.")
    else:
        # 18. 새 글 저장 모드
        response = msgbox.askokcancel("저장", "새 글을 저장하시겠습니까?")
        if response:
            if not os.path.exists("./writing.json"):
                with open("./writing.json", "w", encoding="utf-8") as f:
                    json.dump([], f)

            writing_list = load_writing_json()
            dict_data = {
                "title": title,
                "content": content,
            }
            writing_list.append(dict_data)

            with open("./writing.json", "w", encoding="utf-8") as f:
                json.dump(writing_list, f, ensure_ascii=False, indent=4)

            title_entry.delete(0, END)
            content_text.delete("1.0", END)
            print_listbox()
            msgbox.showinfo("완료", "새 글이 저장되었습니다.")


# 19. 선택된 글 삭제하는 함수
def delete_click():
    global current_editing_index

    index_tuple = listbox.curselection()  # 20. 선택된 항목의 인덱스 가져오기
    if not index_tuple:
        return

    # 21. 삭제 확인 메시지
    response = msgbox.askokcancel("삭제", f"{listbox.get(index_tuple[0])} 삭제하시겠습니까?")
    if response:
        writing_list = load_writing_json()
        writing_list.pop(index_tuple[0])  # 22. 해당 인덱스 글 삭제

        with open("./writing.json", "w", encoding="utf-8") as f:
            json.dump(writing_list, f, ensure_ascii=False, indent=4)

        # 23. 삭제된 글이 현재 편집 중이던 글이면 편집 상태 취소
        if current_editing_index == index_tuple[0]:
            current_editing_index = None
            title_entry.delete(0, END)
            content_text.delete("1.0", END)
            update_ui_state()

        print_listbox()


# 24. 선택된 글을 입력창에 불러오는 함수
def load_click():
    global current_editing_index

    index_tuple = listbox.curselection()
    if not index_tuple:
        return

    if not os.path.exists("./writing.json"):
        return

    writing_list = load_writing_json()
    selected_data = writing_list[index_tuple[0]]

    # 25. 현재 편집 중인 글의 인덱스 저장
    current_editing_index = index_tuple[0]

    # 26. 기존 내용 지우고 선택된 글 내용으로 채우기
    title_entry.delete(0, END)
    title_entry.insert(0, selected_data["title"])

    content_text.delete("1.0", END)
    content_text.insert("1.0", selected_data["content"])

    update_ui_state()  # 27. UI를 수정 모드로 변경


def button_click():
    title = title_entry.get()
    content = content_text.get("1.0", END).strip()
    print(f"제목: {title}, 내용: {content}")


# 28. 모든 버튼들 생성
button = Button(left_frame, text="확인", width=30, command=button_click)
button.pack(pady=5)

save_button = Button(left_frame, text="저장", width=30, command=save_click)
save_button.pack(pady=5)

delete_button = Button(right_frame, text="선택 삭제", width=30, command=delete_click)
delete_button.pack(pady=5)

load_button = Button(right_frame, text="선택 불러오기", width=30, command=load_click)
load_button.pack(pady=5)

# 29. 프로그램 시작시 기존 글 목록 표시하고 UI 상태 설정
print_listbox()
update_ui_state()

root.mainloop()
