class Rectangle:
    def __init__(self, a=10, b=5):
        self.a = a
        self.b = b

    def calculate_area(self):
        area = self.a * self.b
        return f'Площадь = {area}'
    
    def draw(self):
        for i in range(self.b):
            print('*' * self.a)

class Square(Rectangle):
    def __init__(self, side=3):
        super().__init__(side, side)

class Elevator:
    def __init__(self, a=5, b=3):
        self.a = a
        self.b = b

    def up(self):
        if self.b < self.a:
            self.b += 1
            print(f'Лифт поднимается на {self.b} этаж')
        else:
            print('Лифт не может поднятся выше')

    def down(self):
        if self.b > 1:
            self.b -= 1
            print(f'Лифт опускается на {self.b} этаж')
        else:
            print('Лифт не может опустится ниже')

class NewElevator(Elevator):
    def __init__(self, a=5, b=3):
        super().__init__(a, b)
    
    def move(self, floor):
        if floor < 1 or floor > self.a:
            print('Неправельный номер этажа')
        else:
            print(f'Лифт отправляется с {self.b} этажа на {floor} этаж')

elevator = NewElevator(10, 1)
elevator.move(10)