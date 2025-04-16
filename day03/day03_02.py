# 컬렉션 자료형: 리스트(list), 튜플(tuple), 딕셔너리(dict), 셋(set)
# 여러개의 값을 한번에 관리 하려고 -> 관리하기 위해서 반복 가능한 구조

# 리스트 [ ]
성씨들 = ["김", "이", "박"]  # str 리스트
숫자들 = [1, 2, 3, int(4.0), int("5")]  # int 리스트
불리언들 = [True, False, "김" == "김", 1 >= 2]  # bool리스트

# 문자열 <-> 리스트 문자열과 리스트는 공통점이 많다.(사촌관계)
문자열샘플 = "안녕하세요"
리스트샘플 = ["안", "녕", "하", "세", "요"]
print(문자열샘플[0])
print(리스트샘플[0])
print(문자열샘플[-1])
print(리스트샘플[-1])
# str처럼 list는 인덱스로 순서가 존재하는 자료형.
# 인덱싱(a[0]), 슬라이싱(a[0:5]), 길이(len(a)), 요소존재확인(in 연산자), (+,*)연산자, count 가능.

# 슬라이싱
print(문자열샘플[:2])  # 문자열을 잘라서 줌
print(리스트샘플[:2])  # 리스트를 잘라서 줌

# len() : 길이
print(len(문자열샘플))  # 문자열 길이
print(len(리스트샘플))  # 리스트 길이

# in 연산자 : 존재 체크
print("안" in 문자열샘플)  # 문자열에 "안" 문자가 있는가?
print("안" in 리스트샘플)  # list에 "안" 이 있는가?

# 리스트에는 아무거나 넣을 수 있습니다.
자료형짬뽕들 = ["김", 1, 5.5, True]

# 리스트안에 리스트도 가능하다
일학년 = [["김철수", "김영희"], ["이철수", "이영희"], ["박철수", "박영희"]]

# 박철수 -> 일학년 2반 0번
print(일학년[2][0])

# 실습) 주문 응대하기
# 주문이 메뉴판에 있을경우 print("주문이 완료되었습니다")
# 주문이 메뉴판에 없을경우 print("해당 메뉴는 없습니다") 를 출력해주세요

메뉴판 = ["햄버거", "피자", "샐러드", "스파게티", "맥주"]
주문 = "햄버거"

if 주문 in 메뉴판:
    print("주문이 완료되었습니다")
else:
    print("해당 메뉴는 없습니다")

# 리스트 요소를 다루는 방법
냉장고 = ["사과", "바나나", "포도", "수박"]

# 요소 접근(인덱싱)
print(냉장고[0])  # 사과
print(냉장고[-1])  # 수박
print(냉장고[0][0])  # 사

# 요소 변경
냉장고[0] = "토마토"
print(냉장고)

# 요소 추가
냉장고.append("사과")
print(냉장고)  # 마지막 자리에 추가
냉장고.insert(0, "망고")
print(냉장고)  # 특정 위치에 추가(기존 요소들은 뒤로 밀려남)

# 요소 삭제
냉장고.remove("망고")  # 특정 값 삭제 (여러개 있으면 제일 앞에 있는 망고만 삭제)
냉장고.pop()  # 특정 인덱스(위치) 요소 삭제, 생략할 경우 마지막 요소 삭제

# pop은 꺼내오는것 , del은 삭제
김치냉장고 = ["배추김치", "깍두기", "갓김치", "파김치"]
냉장고제일뒤에있던김치 = 김치냉장고.pop()  # 파김치 꺼내옴
print(냉장고제일뒤에있던김치)
# 리스트 연산자

# 리스트끼리 더하기
하나둘셋 = [1, 2, 3]
넷다섯여섯 = [4, 5, 6]
print(하나둘셋 + 넷다섯여섯)
# 새 list를 만들어서 list1과 list2를 담아서 줌 -> 원본(list1, list2)변경된게 아님

하나둘셋.extend(넷다섯여섯)
print(하나둘셋)
# list 자체가 바뀌는것 -> 원본(list1)이 변경됨

# 리스트 곱하기
print(하나둘셋 * 2)
