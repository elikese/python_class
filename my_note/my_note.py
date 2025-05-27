from tkinter import *
from tkinter import messagebox

# 창 설정
root = Tk()
root.title("my note")
root.geometry("720x360")
root.resizable(False, False)

left_frame = Frame(root, width=360, height=360, bg="black")
left_frame.propagate(False)
left_frame.pack(side="left")

right_frame = Frame(root, width=360, height=360, bg="red")
right_frame.propagate(False)
right_frame.pack(side="left")

# 제목
title_label = Label(left_frame, text="제목을 입력하세요")
title_label.pack(pady=10)
title_entry = Entry(left_frame, width=35)
title_entry.pack(pady=5)

# 내용
content_label = Label(left_frame, text="내용을 입력하세요")
content_label.pack(pady=10)
content_text = Text(left_frame, height=12, width=35)
content_text.pack(pady=5)

#
list_label = Label(right_frame, text="저장 목록")
list_label.pack(pady=5)
listbox = Listbox(right_frame, selectmode=EXTENDED, height=15, width=35)
listbox.pack(pady=5, padx=10)


def save_file():
    title = title_entry.get().strip()
    content = content_text.get("1.0", END).strip()

    if not title:
        messagebox.showwarning("경고", "제목을 입력하세요!")
        return
    if not content:
        messagebox.showwarning("경고", "내용을 입력하세요!")
        return

    confirm = messagebox.askyesno("저장 확인", f"'{title}.txt' 파일로 저장할까요?")
    if confirm:
        with open(f"{title}.txt", "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("성공", "파일이 저장되었습니다.")

        # 초기화
        title_entry.delete(0, END)
        content_text.delete("1.0", END)


def delete_file():
    pass


def load_file():
    pass


btn_frame = Frame(right_frame)
btn_frame.pack(pady=10)

btn_save = Button(left_frame, text="저장", width=8, command=save_file)
btn_save.pack(pady=5)

btn_load = Button(btn_frame, text="불러오기", width=8, command=load_file)
btn_load.grid(row=0, column=1, padx=5)

btn_delete = Button(btn_frame, text="삭제", width=8, command=delete_file)
btn_delete.grid(row=0, column=2, padx=5)


root.mainloop()
