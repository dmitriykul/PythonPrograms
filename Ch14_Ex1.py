class Square():
    square_list = []
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)

r1 = Square(3)
r2 = Square(5)
r3 = Square(4)
print(Square.square_list)
