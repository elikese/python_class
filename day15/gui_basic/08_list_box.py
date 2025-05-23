from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

# selectmode = SINGLE:하나만선택가능, EXTENDED:여러개선택가능
listbox = Listbox(root, selectmode=EXTENDED, height=3)
# height가 0이면 요소 전체 다 보여줌
# height가 0이 아니면 지정한 숫자만큼만 보여 줌
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박", "포도")  # END: 제일 마지막index, *arg매개변수
listbox.pack()


def click():
    # listbox.delete(END)  # index자리에 0:처음, END:마지막
    print(listbox.size())  # 총 갯수 리턴
    print(listbox.get(0, END))  # 항목확인
    print(listbox.curselection())  # 선택된 항목들 index들을 튜플로 리턴
    pass


# 실습
# 버튼을 눌렀을때 내가 선택한 항목들이 출력되게
# 만들어 주세요
def seek():
    select_indices = listbox.curselection()
    print(select_indices)
    for index in select_indices:
        print(listbox.get(index))


# [0, 1, 2, 3, 4] 2,3번 삭제
# [0, 1, 3] 낮은 index 순으로 삭제할 경우
# [0, 1, 4] 높은 index 순으로 삭제할 경우 -> 의도한 것
def delete():
    select_indices = listbox.curselection()
    # sorted(select_indices, reverse=True) -> 새 배열을 리턴, 원본을 바꾸는게 아니에요
    for index in reversed(select_indices):
        listbox.delete(index)


btn1 = Button(root, text="클릭", command=click)
btn1.pack()

btn2 = Button(root, text="확인", command=seek)
btn2.pack()

btn3 = Button(root, text="삭제", command=delete)
btn3.pack()

root.mainloop()
