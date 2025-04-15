# 실습) 장바구니에 상품 담기
# input을 통해 내가 원하는 상품 3개(item1 ~ item3)을 입력하고
# cart에 담아서 print 해주세요
cart = []
item1 = input("카트에 담을 상품:")
item2 = input("카트에 담을 상품:")
item3 = input("카트에 담을 상품:")

# item을 cart에 담는 코드
cart.append(item1)
cart.append(item2)
cart.append(item3)
cart = [item1, item2, item3]
cart.extend([item1, item2, item3])

print(item1, item2, item3)
print(f"장바구니 목록: {cart}")
