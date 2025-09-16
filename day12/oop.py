class Student:
    def __init__(self, name, korean, english, math):
        if not isinstance(name, str):
            print("이름은 문자열이어야 합니다.")
            return

        for score in (korean, english, math):
            if not isinstance(score, int):
                print("점수는 정수여야 합니다.")
                return
            if score < 0 or score > 100:
                print("점수는 0~100 사이여야 합니다.")
                return

        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def total_score(self):
        return self.korean + self.english + self.math

    def average_score(self):
        return self.total_score() / 3


class School:
    def __init__(self, name):
        if not isinstance(name, str):
            print("학교 이름은 문자열이어야 합니다.")
            return
        self.name = name
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            print("학생만 추가할 수 있습니다.")
            return
        self.students.append(student)

    def print_students(self):
        for stu in self.students:
            print(stu.name, f"총점: {stu.total_score()}", f"평균: {stu.average_score()}")

    # 실습 반평균을 구하는 메서드를 정의해주세요
    def class_average(self):
        if not self.students:
            print("학생이 없습니다.")
            return
        total = 0
        for stu in self.students:
            total += stu.average_score()
        print("전체 학생 평균:", total / len(self.students))


s1 = Student("철수", 90, 85, 70)
s2 = Student("영희", 100, 95, 80)

school = School("서울중학교")
school.add_student(s1)
school.add_student(s2)

school.print_students()
school.class_average()
