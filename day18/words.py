from tkinter import *
from tkinter import ttk
import json
import os

words = []
index = 0
is_revealed = False
selected_index = None
data_path = "words.json"


def load_words():
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_words():
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)


def show_word():
    global is_revealed
    if words:
        word = words[index]
        label_mem.config(text=word["meaning"])
        is_revealed = False
    else:
        label_mem.config(text="단어 없음")


def reveal_word():
    global is_revealed
    if words and not is_revealed:
        label_mem.config(text=words[index]["english"])
        is_revealed = True


def next_word():
    global index
    if words:
        index = (index + 1) % len(words)
        show_word()


def refresh_word_list():
    listbox.delete(0, END)
    for word in words:
        listbox.insert(END, f"{word['english']} - {word['meaning']}")


def on_listbox_select(event):
    global selected_index
    try:
        selected_index = listbox.curselection()[0]
        word = words[selected_index]
        entry_eng.delete(0, END)
        entry_eng.insert(0, word["english"])
        entry_kor.delete(0, END)
        entry_kor.insert(0, word["meaning"])
    except IndexError:
        selected_index = None


def add_word():
    eng = entry_eng.get()
    kor = entry_kor.get()
    if eng and kor:
        words.append({"english": eng, "meaning": kor, "memorized": False})
        save_words()
        entry_eng.delete(0, END)
        entry_kor.delete(0, END)
        refresh_word_list()


def update_word():
    global selected_index
    if selected_index is not None:
        new_eng = entry_eng.get()
        new_kor = entry_kor.get()
        if new_eng and new_kor:
            words[selected_index] = {"english": new_eng, "meaning": new_kor, "memorized": False}
            save_words()
            refresh_word_list()


def delete_word():
    global selected_index
    if selected_index is not None:
        del words[selected_index]
        save_words()
        entry_eng.delete(0, tk.END)
        entry_kor.delete(0, tk.END)
        selected_index = None
        refresh_word_list()


# === UI ===
root = Tk()
root.title("영단어 암기앱")
root.geometry("300x450")

words = load_words()

# 탭 추가
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# === 암기 탭 ===
frame_memorize = Frame(notebook)
notebook.add(frame_memorize, text="퀴즈")

label_mem = Label(frame_memorize, text="", font=("Arial", 16, "bold"))
label_mem.pack(pady=20)

Button(frame_memorize, text="정답 보기", command=reveal_word).pack(pady=5)
Button(frame_memorize, text="다음 단어", command=next_word).pack(pady=5)

# === 관리 탭 ===
frame_manage = Frame(notebook)
notebook.add(frame_manage, text="단어 관리")

entry_eng = Entry(frame_manage)
entry_eng.pack(pady=5)

entry_kor = Entry(frame_manage)
entry_kor.pack(pady=5)

Button(frame_manage, text="추가", command=add_word).pack(pady=5)
Button(frame_manage, text="수정", command=update_word).pack(pady=5)
Button(frame_manage, text="삭제", command=delete_word).pack(pady=5)

list_frame = Frame(frame_manage)
list_frame.pack(fill="both", expand=True, pady=10)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(list_frame, height=10, yscrollcommand=scrollbar.set)
listbox.pack(side="left", fill="both", expand=True)
listbox.bind("<<ListboxSelect>>", on_listbox_select)

scrollbar.config(command=listbox.yview)

# 초기 상태
refresh_word_list()
show_word()

root.mainloop()
