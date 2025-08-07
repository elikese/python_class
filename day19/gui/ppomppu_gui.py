# 크롤링 교육용 - GUI 인터페이스
# tkinter를 사용한 데스크톱 애플리케이션 구현 예제

from tkinter import *  # tkinter의 모든 클래스와 함수 임포트
import tkinter.messagebox as msgbox  # 알림창(메시지박스) 사용
import os  # 운영체제 관련 기능 (파일 열기, 삭제 등)
import glob  # 파일 패턴 검색 (*.xlsx 파일들 찾기)
from ppomppu_crawler import crawl_multiple_pages, save_to_excel, generate_filename

# =============================================================================
# GUI 메인 윈도우 설정
# =============================================================================
root = Tk()  # 메인 윈도우 생성
root.geometry("800x500")  # 창 크기 설정 (가로x세로)
root.title("뽐뿌 크롤러")  # 창 제목 설정
root.resizable(False, False)  # 창 크기 조절 비활성화 (가로, 세로)

# =============================================================================
# 화면 레이아웃 구성 - 좌우 분할
# =============================================================================
# 왼쪽 프레임: 크롤링 관련 기능
left_frame = Frame(root, width=500, height=500)
left_frame.propagate(False)  # 자동 크기 조절 방지 (고정 크기 유지)
left_frame.pack(side=LEFT)  # 왼쪽에 배치

# 오른쪽 프레임: 파일 관리 기능
right_frame = Frame(root, width=250, height=500)
right_frame.propagate(False)
right_frame.pack(side=LEFT)

# =============================================================================
# 왼쪽 프레임: 크롤링 인터페이스
# =============================================================================
# 제목 라벨
title_label = Label(left_frame, text="뽐뿌 게시글 크롤러", font=("맑은 고딕", 18, "bold"))
title_label.pack(pady=10)  # 상하 여백 10px

# 페이지 수 입력부
page_label = Label(left_frame, text="크롤링할 페이지 수")
page_label.pack(pady=5)
page_entry = Entry(left_frame, width=10)  # 입력창 생성
page_entry.pack(pady=5)
page_entry.insert(0, "3")  # 기본값 "3" 설정

# 크롤링 시작 버튼
crawl_button = Button(left_frame, text="크롤링 시작", width=30)
crawl_button.pack(pady=5)

# 진행상황 표시부
progress_label = Label(left_frame, text="진행상황")
progress_label.pack(pady=(20, 5))  # 위쪽 20px, 아래쪽 5px 여백
progress_text = Text(left_frame, width=60, height=16)  # 다중행 텍스트 위젯
progress_text.pack(pady=5)

# 엑셀 저장 버튼 (초기에는 비활성화 상태)
save_button = Button(left_frame, text="엑셀로 저장", width=30, state=DISABLED)
save_button.pack(pady=10)

# =============================================================================
# 오른쪽 프레임: 파일 관리 인터페이스
# =============================================================================
# 파일 목록 제목
file_label = Label(right_frame, text="저장된 파일", font=("맑은 고딕", 16, "bold"))
file_label.pack(pady=10)

# 파일 목록 리스트박스 (단일 선택 모드)
file_listbox = Listbox(right_frame, width=35, height=18, selectmode=SINGLE)
file_listbox.pack(pady=5)

# 파일 관리 버튼들
refresh_button = Button(right_frame, text="새로고침", width=35)
refresh_button.pack(pady=5)

open_button = Button(right_frame, text="파일 열기", width=35)
open_button.pack(pady=5)

delete_button = Button(right_frame, text="선택 삭제", width=35)
delete_button.pack(pady=5)

# =============================================================================
# 전역 변수
# =============================================================================
crawl_data = []  # 크롤링된 데이터를 저장할 리스트 (함수들 간 데이터 공유용)


# =============================================================================
# GUI 이벤트 처리 함수들
# =============================================================================


def log_message(message):
    """
    진행상황을 텍스트박스에 출력하는 함수
    - 크롤러의 logger 매개변수로 전달됨
    - 크롤링 진행상황을 실시간으로 사용자에게 보여줌
    """
    progress_text.insert(END, f"{message}\n")  # 텍스트 끝에 메시지 추가
    progress_text.see(END)  # 스크롤을 맨 아래로 이동
    root.update()  # GUI 즉시 업데이트 (실시간 표시)


def load_file_list():
    """
    저장된 엑셀 파일 목록을 리스트박스에 표시하는 함수
    - 현재 폴더에서 '뽐뿌게시글_*.xlsx' 패턴의 파일들을 찾아서 표시
    - 파일 크기 정보도 함께 표시
    """
    file_listbox.delete(0, END)  # 기존 목록 모두 삭제

    # glob은 file 이름 패턴을 매칭해서 file 이름들을 문자열로 바꿔서 가져옴
    # glob을 사용해서 패턴에 맞는 파일들 찾기
    excel_file_names = glob.glob("뽐뿌게시글_*.xlsx")
    excel_file_names.sort(reverse=True)  # 최신 파일이 위로 오도록 역순 정렬

    for excel_file_name in excel_file_names:
        # 파일 크기 계산 (바이트 → KB)
        size = os.path.getsize(excel_file_name)
        size_kb = size // 1024
        # 파일명과 크기를 함께 표시
        file_listbox.insert(END, f"{excel_file_name} ({size_kb}KB)")


def start_crawl():
    """
    크롤링을 시작하는 함수
    - 사용자 입력 검증
    - 크롤러 함수 호출
    - 결과에 따른 UI 상태 변경
    """
    global crawl_data  # 전역 변수 사용 선언

    # 1. 사용자 입력 검증
    try:
        page_count = int(page_entry.get())  # 입력값을 정수로 변환
        if page_count <= 0:
            msgbox.showerror("오류", "페이지 수는 1 이상이어야 합니다.")
            return
    except ValueError:  # 숫자가 아닌 값 입력시 발생
        msgbox.showerror("오류", "올바른 페이지 수를 입력해주세요.")
        return

    # 2. UI 상태 변경 (크롤링 중임을 표시)
    crawl_button.config(state=DISABLED)  # 크롤링 버튼 비활성화 (중복 실행 방지)
    save_button.config(state=DISABLED)  # 저장 버튼 비활성화
    progress_text.delete(1.0, END)  # 이전 로그 내용 삭제

    log_message(f"{page_count}페이지 크롤링을 시작합니다...")

    try:
        # 3. 실제 크롤링 실행
        # crawl_multiple_pages()는 (데이터리스트, 결과메시지) 튜플을 반환
        crawl_data, result_message = crawl_multiple_pages(page_count, log_message)
        #    ↑ 데이터       ↑ 결과메시지              ↑ 페이지수    ↑ 로거함수

        # 4. 크롤링 결과 처리
        if crawl_data:  # 데이터가 있으면 성공
            log_message(result_message)  # "총 X개 게시글 수집 완료" 메시지 출력
            log_message("크롤링이 완료되었습니다! 저장 버튼을 눌러주세요.")
            save_button.config(state=NORMAL)  # 저장 버튼 활성화
        else:  # 데이터가 없으면 실패
            log_message(f"크롤링 실패: {result_message}")  # 에러 메시지 출력

    except Exception as e:
        # 5. 예상치 못한 오류 처리
        log_message(f"오류 발생: {e}")

    finally:
        # 6. 작업 완료 후 UI 복구 (성공/실패 관계없이 실행)
        crawl_button.config(state=NORMAL)  # 크롤링 버튼 다시 활성화


def save_excel():
    """
    크롤링된 데이터를 엑셀 파일로 저장하는 함수
    - 전역변수 crawl_data에 저장된 데이터를 엑셀로 변환
    - 저장 완료 후 파일 목록 새로고침
    """
    global crawl_data

    # 1. 저장할 데이터가 있는지 확인
    if not crawl_data:
        msgbox.showerror("오류", "저장할 데이터가 없습니다.")
        return

    # 2. 파일명 생성 (타임스탬프 포함)
    filename = generate_filename()  # "뽐뿌게시글_20250807_143025.xlsx" 형식

    # 3. 엑셀 저장 실행
    # save_to_excel()는 (성공여부, 메시지) 튜플을 반환
    success, message = save_to_excel(crawl_data, filename)
    #   ↑ True/False    ↑ 결과메시지

    # 4. 저장 결과 처리
    if success:  # 저장 성공시
        log_message(message)  # "엑셀 파일 저장 완료: 파일명" 메시지 출력
        msgbox.showinfo("완료", f"엑셀 파일이 저장되었습니다!\n파일명: {filename}")
        load_file_list()  # 파일 목록 새로고침 (새로 저장된 파일 표시)
    else:  # 저장 실패시
        log_message(f"저장 실패: {message}")
        msgbox.showerror("오류", f"저장에 실패했습니다: {message}")


def open_file():
    """
    리스트박스에서 선택된 엑셀 파일을 기본 프로그램으로 여는 함수
    - Windows: Excel, Mac: Numbers 등으로 자동 실행
    """
    # 1. 선택된 항목 확인
    index_tuple = file_listbox.curselection()  # 선택된 항목의 인덱스 튜플 반환
    if not index_tuple:  # 선택된 항목이 없으면
        msgbox.showwarning("알림", "열 파일을 선택해주세요.")
        return

    # 2. 선택된 파일명 추출
    file_text = file_listbox.get(index_tuple[0])  # 선택된 항목의 텍스트 가져오기
    filename = file_text.split(" (")[0]  # "파일명.xlsx (123KB)" → "파일명.xlsx"

    # 3. 운영체제별 파일 열기 시도
    try:
        os.startfile(filename)  # Windows에서 기본 프로그램으로 파일 열기
    except:
        try:
            os.system(f"open {filename}")  # Mac에서 기본 프로그램으로 파일 열기
        except:
            msgbox.showerror("오류", "파일을 열 수 없습니다.")


def delete_file():
    """
    리스트박스에서 선택된 엑셀 파일을 삭제하는 함수
    - 삭제 확인 후 실제 파일 삭제
    - 삭제 후 파일 목록 새로고침
    """
    # 1. 선택된 항목 확인
    index_tuple = file_listbox.curselection()
    if not index_tuple:
        msgbox.showwarning("알림", "삭제할 파일을 선택해주세요.")
        return

    # 2. 선택된 파일명 추출
    file_text = file_listbox.get(index_tuple[0])
    filename = file_text.split(" (")[0]

    # 3. 삭제 확인
    response = msgbox.askokcancel("삭제", f"{filename}을 삭제하시겠습니까?")
    if response:  # 사용자가 "확인" 선택시
        try:
            os.remove(filename)  # 실제 파일 삭제
            load_file_list()  # 파일 목록 새로고침
            msgbox.showinfo("완료", "파일이 삭제되었습니다.")
        except Exception as e:
            msgbox.showerror("오류", f"파일 삭제 실패: {str(e)}")


# =============================================================================
# 이벤트 연결 (버튼 클릭시 실행할 함수 지정)
# =============================================================================
crawl_button.config(command=start_crawl)  # 크롤링 시작 버튼
save_button.config(command=save_excel)  # 엑셀 저장 버튼
refresh_button.config(command=load_file_list)  # 새로고침 버튼
open_button.config(command=open_file)  # 파일 열기 버튼
delete_button.config(command=delete_file)  # 파일 삭제 버튼

# =============================================================================
# 프로그램 초기화 및 실행
# =============================================================================
load_file_list()  # 프로그램 시작시 기존 파일 목록 로드
root.mainloop()  # GUI 이벤트 루프 시작 (프로그램 종료까지 대기)


# =============================================================================
# GUI 프로그래밍 개념 설명:
#
# 1. 이벤트 기반 프로그래밍:
#    - 사용자의 행동(버튼 클릭, 텍스트 입력 등)에 반응해서 함수 실행
#    - 콜백 함수: 이벤트 발생시 자동으로 호출되는 함수
#
# 2. 함수간 데이터 공유:
#    - 전역 변수: 모든 함수에서 접근 가능한 변수 (crawl_data)
#    - 함수 반환값: 튜플을 사용해서 여러 값 동시 반환
#
# 3. UI 상태 관리:
#    - 버튼 활성화/비활성화로 사용자 행동 제어
#    - 실시간 피드백으로 사용자 경험 향상
#
# 4. 에러 처리:
#    - try-except로 예상 가능한 오류 처리
#    - 사용자 친화적인 에러 메시지 제공
# =============================================================================
