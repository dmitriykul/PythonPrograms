class Triangle():
    def __init__(self, a, h):
        self.high = h
        self.a = a
        
    def calculate_area(self):
        return 0.5 * self.high * self.a

a_Triangle = Triangle(10, 20)
print(a_Triangle.calculate_area())
