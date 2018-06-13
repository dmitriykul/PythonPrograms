#Пример композиции
class Horse():
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

Nack = Horse('Нэк', 'черный')
Stan = Rider('Стен Роуз', Nack)

print(Stan.horse.name)
    
