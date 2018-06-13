#Подсчитывание площади круга с помощью объектно ориентированного программирования
import math
class Circle():
    def __init__(self, r):
        self.radius = r

    def calculate_area(self):
        return self.radius ** 2 * math.pi

circle = Circle(10)
print(circle.calculate_area())
