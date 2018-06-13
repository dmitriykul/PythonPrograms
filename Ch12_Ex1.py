#Класс Apple с четырьмя переменными экземпляра, свойства яблока
class Apple:
    def __init__(self, w, c):
        """Вес в граммах"""
        self.weight = w
        self.color = c
        self.mold = 0
        print('Создано')

    def rot(self, days, temp):
        self.mold = days * temp

apple = Apple(6, 'Зеленое')
print(apple.color)
apple.rot(10, 33)
print(apple.mold)
