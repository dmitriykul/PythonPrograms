class Square:
    def __init__(self, s1):
        self.s1 = s1
        
    def __repr__(self):
        return "{} на {} на {} на {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
print(a_square)
