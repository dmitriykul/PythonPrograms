#Словарь
Dict={'Рост': 182,
      'Любимый цвет': 'Красный',
      'Любимый актер': 'Рами Малек',
    }

charc=input('Введите параметр: Рост, Любимый цвет или актер ')
if charc in Dict:
    charc = Dict[charc]
    print(charc)
else:
    print('Не найдено')
