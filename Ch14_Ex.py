#Функция, проверяющая одинаковость двух объектов
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

def Is(C1, C2):
    return C1 is C2

a_rectangle = Rectangle(10, 20)
b_rectangle = a_rectangle
print(Is(a_rectangle, b_rectangle))
