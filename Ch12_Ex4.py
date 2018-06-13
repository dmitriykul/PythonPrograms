#Подсчитывание периметра шестиугольника
class Hexagon():
    def __init__(self, s):
        self.base = s

    def calculate_perimetr(self):
        return self.base * 6

a_hexagon = Hexagon(10)
print(a_hexagon.calculate_perimetr())
