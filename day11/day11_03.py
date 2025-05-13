class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def print_car(self):
        print(f"모델명:{self.model}, 색상:{self.color}")


car1 = Car("소나타", "흰색")

car1.print_car()

# 속성을 변경하려면?
car1.color = "검정"
