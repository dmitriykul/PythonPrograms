#Площадь треугольника и квадрата

class Rectangle():

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def calculate_perimetr(self):
        print('Периметр равен: ', self.a1 * 2 + self.a2 * 2)

class Square():

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def calculate_perimetr(self):
        print('Периметр равен: ', self.a1 + self.a2 + self.a3 + self.a4)

    def change_size(self, N):
        self.N = N
        self.a1 += N
        self.a2 += N
        self.a3 += N
        self.a4 += N

a_rectangle = Rectangle(2,3)
a_rectangle.calculate_perimetr()

a_square = Square(2,2,2,2)
a_square.calculate_perimetr()
a_square.change_size(1)
a_square.calculate_perimetr()
