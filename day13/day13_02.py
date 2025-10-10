class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __getitem__(self, key):
        # 특별한 키워드로 계산된 값 반환
        if key == "birth_year":
            return 2025 - self.age
        elif key == "adult":
            return self.age >= 20
        elif key == "category":
            if self.age < 20:
                return "청소년"
            elif self.age < 60:
                return "성인"
            else:
                return "시니어"
        return None


# 사용 예시
person = Person("홍길동", 25, "개발자")
print(person["name"])  # 홍길동
print(person["birth_year"])  # 2000 (계산된 값!)
print(person["adult"])  # True
print(person["category"])  # 성인


class Config:

    def __init__(self):
        self.data = {"host": "www.naver.com", "port": 443}

    def __getitem__(self, key):
        if key == "url":
            # 두 값을 합쳐서 새로운 값 생성
            return f"http://{self.data['host']}:{self.data['port']}"
        elif key == "debug_info":
            return f"서버: {self.data['host']}, 포트: {self.data['port']}"
        else:
            return self.data.get(key)


# 사용 예시
config = Config()
print(config["host"])  # localhost
print(config["url"])  # http://localhost:8080 (조합된 값!)
print(config["debug_info"])  # 서버: localhost, 포트: 8080
print(config["1212"])


# 실습 문제:
"""
Person 클래스를 완성하여 다음과 같이 동작하도록 구현하세요.

person1 = Person("991225-1234567")
person2 = Person("021115-2345678")

print(person1["gender"])     # 남성
print(person1["birth_year"]) # 1999
print(person1["birthday"])   # 12월 25일

print(person2["gender"])     # 여성  
print(person2["birth_year"]) # 2002
print(person2["birthday"])   # 11월 15일
"""


class Person:
    def __init__(self, ssn):
        self.ssn = ssn  # "991225-1234567" 형태

    def __getitem__(self, key):
        if key == "gender":
            # 뒷자리 첫 번째 숫자로 성별 판단
            gender_num = int(self.ssn[7])
            if gender_num in [1, 3]:
                return "남성"
            elif gender_num in [2, 4]:
                return "여성"
            else:
                return "알 수 없음"

        elif key == "birth_year":
            # 앞 2자리로 태어난 연도 계산
            year = int(self.ssn[:2])
            gender_num = int(self.ssn[7])
            if gender_num in [1, 2]:  # 1900년대
                return 1900 + year
            elif gender_num in [3, 4]:  # 2000년대
                return 2000 + year

        elif key == "birthday":
            # MMDD 형태로 생일 추출
            month = self.ssn[2:4]
            day = self.ssn[4:6]
            return f"{month}월 {day}일"

        else:
            return "지원하지 않는 정보입니다"


# __call__()
class EventLogger:
    def __init__(self, name):
        self.name = name
        self.logs = []

    def __call__(self, message, level="INFO"):
        import datetime

        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.logs.append(log_entry)
        print(f"{self.name} - {log_entry}")


# 사용 예시
logger = EventLogger("시스템")
logger("서버 시작됨")  # 함수처럼 호출!
logger("오류 발생", "ERROR")
logger("작업 완료")
