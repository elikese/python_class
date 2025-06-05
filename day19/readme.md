exe 변환 방법
PyInstaller 사용 (권장)

먼저 PyInstaller 설치:
bash
pip install pyinstaller
exe 파일 생성:
bash
pyinstaller --onefile --windowed hamburger_app.py
옵션 설명:

--onefile: 하나의 exe 파일로 생성
--windowed: 콘솔 창 없이 GUI만 표시
dist 폴더에서 생성된 exe 파일 확인

pip install requests
pip install openpyxl
pip install beautifulsoup4