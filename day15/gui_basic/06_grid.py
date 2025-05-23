from tkinter import *

# 창 만들기
root = Tk()  # 창 생성(클래스)
root.title("연습")  # 창 이름(타이틀)
root.geometry("300x400")  # 창크기 (가로x세로)
root.resizable(False, False)  # 창 크기 조절가능 여부(가로, 세로)

# pack, place, grid
# 1. pack
# 알아서 위에서 아래로, 좌에서 우로, 아래에서 위로... 적재
# 간단하게 배치할때는 좋음. 세밀한 위치 조정 x

# 2. place
# 절대좌표로 정확한 위치에 배치(픽셀 단위로)
# 위젯이 많아지면 복잡하다.

# 3. grid
# 엑셀같은 표와 같은 형식
# 격자 구조로 배치
# 깔끔하고, 복잡해도 깔끔하게 정리가능

# grid
# Button(button_frame, text="1", height=5, width=8).grid(row=0, column=0)
# Button(button_frame, text="2", height=5, width=8).grid(row=0, column=1)
# Button(button_frame, text="3", height=5, width=8).grid(row=0, column=2)
# Button(button_frame, text="4", height=5, width=8).grid(row=0, column=3)

button_frame = Frame(root)
button_frame.place(
    relx=0.5, rely=0.5, anchor=CENTER
)  # anchor-> 기준점, relx, rely => 상대적인 좌표

# 계산기
Button(button_frame, text="clear", width=8, height=5).grid(
    row=1, column=0, sticky="nsew", padx=3, pady=3
)  # clear로 수정
Button(button_frame, text="/", width=8, height=5).grid(
    row=1, column=1, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="*", width=8, height=5).grid(
    row=1, column=2, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="-", width=8, height=5).grid(
    row=1, column=3, sticky="nsew", padx=3, pady=3
)

Button(button_frame, text="7", width=8, height=5).grid(
    row=2, column=0, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="8", width=8, height=5).grid(
    row=2, column=1, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="9", width=8, height=5).grid(
    row=2, column=2, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="+", width=8, height=5).grid(
    row=2, column=3, sticky="nsew", padx=3, pady=3
)

Button(button_frame, text="4", width=8, height=5).grid(
    row=3, column=0, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="5", width=8, height=5).grid(
    row=3, column=1, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="6", width=8, height=5).grid(
    row=3, column=2, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="enter", width=8, height=5).grid(
    row=3, column=3, rowspan=2, sticky="nsew", padx=3, pady=3
)

Button(button_frame, text="1", width=8, height=5).grid(
    row=4, column=0, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="2", width=8, height=5).grid(
    row=4, column=1, sticky="nsew", padx=3, pady=3
)
Button(button_frame, text="3", width=8, height=5).grid(
    row=4, column=2, sticky="nsew", padx=3, pady=3
)

root.mainloop()

# 비슷한 버튼들이 참 많죠
# 깔끔하게 관리하고 싶죠
# 2차원 배열, 이중 for문 써주면?
# 스타일도 text만 바뀌고 있음
# text만 주입해주는 방식으로 바꿀수 있다면?
