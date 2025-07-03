# *args 패킹 -> 여러값을 하나의 tuple로 묶어서 전달
# **kwargs 패킹 -> 여러값을 하나의 dict로 묶어서 전달
import random


def make_user(username, **details):
    user = {"name": username}
    user.update(details)
    return user


user1 = make_user("홍길동", age=20, 거주지="부산")
print(user1)
user2 = make_user("홍길동", age=20, 거주지="부산", name="박길동")
print(user2)

# **kwarg 언패킹 가능!


def print_user(**kwargs):
    print(kwargs)


# print_user(user1)  # 'key=value' 형태가 아니라서 에러
print_user(**user1)  # 이미 dict로 패킹되어있다고 알려주는것


# 나이 검사
def make_civil(name="", age=0):
    civil = {"name": name, "age": age}
    return civil  # dict


l_names = ["김", "박", "이"]
f_names = ["철수", "영희", "병철", "국진"]
civil_list = []
for l_name in l_names:
    for f_name in f_names:
        full_name = l_name + f_name
        age = random.randint(8, 50)
        civil = make_civil(full_name, age)
        civil_list.append(civil)

print(civil_list)


def minor_filter(**civil):
    if civil["age"] < 20:
        print(f"미성년자! {civil}")


for civil in civil_list:
    minor_filter(**civil)
