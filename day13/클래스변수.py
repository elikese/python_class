
class Student:
    school_name = "Korea IT Academy"  # 클래스 변수
    count = 0                         # 클래스 변수

    def __init__(self, name):
        self.name = name              # 인스턴스 변수
        Student.count += 1

s1 = Student("홍길동")
s2 = Student("김철수")

print(Student.count)     # 2
print(s1.count)          # 2
print(s2.count)          # 2


class Student:
    shared_wallet = 10_000  # 클래스 변수 (공용 지갑)

    def __init__(self, name, my_money):
        self.name = name
        self.my_wallet = my_money  # 인스턴스 변수 (내 지갑)

    def withdraw_from_shared(self, amount):
        """공용 지갑에서 내 지갑으로 돈을 가져온다"""
        if Student.shared_wallet < amount:
            print(f"{self.name}: 공용 지갑에 돈이 부족합니다.")
            return

        Student.shared_wallet -= amount
        self.my_wallet += amount
        print(f"{self.name}이(가) 공용 지갑에서 {amount}원을 가져왔습니다.")

    def spend_my_money(self, amount):
        """내 지갑에서만 소비한다"""
        if self.my_wallet < amount:
            print(f"{self.name}: 내 지갑에 돈이 부족합니다.")
            return

        self.my_wallet -= amount
        print(f"{self.name}이(가) {amount}원을 사용했습니다.")

    def print_status(self):
        print(
            f"{self.name} | 내 지갑: {self.my_wallet} | 공용 지갑: {Student.shared_wallet}"
        )

s1 = Student("홍길동", 1000)
s2 = Student("김철수", 500)

s1.print_status()
s2.print_status()
# 홍길동 | 내 지갑: 1000 | 공용 지갑: 10000
# 김철수 | 내 지갑: 500 | 공용 지갑: 10000

s1.withdraw_from_shared(3000)
s2.print_status()
# 김철수 | 내 지갑: 500 | 공용 지갑: 7000

s1.spend_my_money(2000)
s1.print_status()
# 홍길동 | 내 지갑: 2000 | 공용 지갑: 7000
