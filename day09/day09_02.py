# lambda함수(익명함수, 미시함수)
# def로 선언시 함수에 이름을 만들어주는데, 그럴 필요없이 너무 단순한 구조일 경우
# 주로 매개인자로 함수를 넘기는데, 그 구조가 단순할때
# 단순하다의 기준 : 한줄로 작성 가능 할 때
# 한줄로 복잡할 바에 람다 X, 성능? python에선 일반함수와 람다함수는 성능 동일

# lambda 매개변수: 리턴


def multiply(num1, num2):
    return num1 * num2


print(multiply(5, 5))

lambda_multi = lambda num1, num2: num1 * num2
print(lambda_multi(5, 5))


# 람다와 자주 같이 쓰이는 내장함수
# 이 내장함수들은 매개변수로 함수를 받는 함수들

# 1. filter(): 함수 결과가 True인 것만 남김, 최종적으로 list로 형변환
# filter( bool을 리턴하는 함수 , 순서가 있는 자료형(list,tuple...) )
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))

food_list = ["계란", "우유(상함)", "김치", "사과", "치즈(상함)", "된장국"]
# 기존에는 반복문으로 순회하면서 if문에 걸린것들 따로 담아서 찾아냄
filtered_food_list = list(filter(lambda food: "상함" in food, food_list))
print(filtered_food_list)

# 실습) 짝수리스트에 홀수가 끼여있다.
# filter를 통해 홀수들을 찾아내서 출력하세요
evens = [2, 4, 6, 12, 26, 35, 55, 10]
print(list(filter(lambda num: num % 2 == 1, evens)))


# 2. map() : 반복 가능한 값 각각에 함수 적용, 최종적으로 list로 형변환
# map( 리스트 요소를 조작하는 함수 , 순서가 있는 자료형(list,tuple...) )
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
food_list = ["계란", "우유(상함)", "김치", "사과", "치즈(상함)", "된장국"]
# 기존에는 반복문으로 순회하면서 if문에 걸리면 수정
mapped_food_list = list(
    map(lambda food: food[:-4] if "상함" in food else food, food_list)
)
print(mapped_food_list)

# 실습) 이름 명단이 있다. 이름 뒤에 모두 ~고객님 이라고 문자열을 수정해야한다.
# map을 통해 수정해주세요
client_names = ["철수", "영희", "민수", "병철", "은희"]
mapped_client_names = list(map(lambda name: name + "고객님", client_names))
print(mapped_client_names)

# 3. sorted(): key 함수 기준으로 정렬
words = ["banana", "kiwi", "apple"]
sorted_words = sorted(words)
print(sorted_words)  # a, b, c 순서로 정렬

sorted_by_len = sorted(words, key=lambda x: len(x))
print(sorted_by_len)  # 단어가 짧은(글자길이) 순서로 정렬

# 4. max(), min(): key 함수 기준으로 최대값, 최솟값
# max, min은 숫자를 대상 연산
print(max(1, 2, 3, 4, 5))  # 5
print(min(1, 2, 3, 4, 5))  # 1
numbers = [10, 20, 30, 40, 50]
print(max(numbers))  # 50 순회가능한 자료형을 매개변수로 받을 수 있음
print(min(numbers))  # 10 순회가능한 자료형을 매개변수로 받을 수 있음

# 이름이 가장 긴걸 찾고 싶을때
names = ["Kim", "Park", "Lee"]
longest_name = max(names, key=lambda x: len(x))  # Park

# key로 여러가지 기준을 만들순 없는가?
# "Kim", "Lee"는 길이 기준으론 동률 -> 동률일때는 a,b,c... 순서로 정렬하고싶다!
longest_name2 = max(names, key=lambda x: (len(x), x))

fruits = [
    {"name": "apple", "price": 1200, "weight": 100},
    {"name": "banana", "price": 800, "weight": 100},
    {"name": "grape", "price": 2500, "weight": 80},
    {"name": "peach", "price": 2500, "weight": 100},
]

# fruits 리스트에 있는 dict에서 가장비싼 과일 찾는다,
# 만약 가장 비싼 가격이 동률이라면, 무게가 가장 많이 나가는걸 찾아주세요

result = max(fruits, key=lambda fruit: (fruit["price"], fruit["weight"]))
print(result)
