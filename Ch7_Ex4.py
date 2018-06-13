#Бесконечный цикл
Num = [1,2,3,4,5,6,7,8,9,0]

print('Введите X для выхода')
while True:
    r = input('Отгадайте число из списка: ')
    if r == 'X' or r == 'x':
        break
    try:
        r = int(r)
    except ValueError:
        print('Введите число или X для выхода.')
    if r in Num:
        print('Вы отгадали правильно')
    else:
        print('Неправильно')
