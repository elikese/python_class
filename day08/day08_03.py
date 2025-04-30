# *args 언패킹 -> 여러값을 하나의 tuple로 묶어서 전달
# **kwargs 언패킹 -> 여러값을 하나의 dict로 묶어서 전달


def make_user(username, **details):
    user = {"name": username}
    user.update(details)
    return user


user1 = make_user("홍길동", age=20, 거주지="부산")
print(user1)
user2 = make_user("홍길동", age=20, 거주지="부산", name="박길동")
print(user2)
