def str(string):
    """Преобразует строка в целое число.
    :параметр string: строка.
    :return: строка, преобразованная в целое число.
    """
    try:
        return float(x)
    except ValueError:
        print('Ошибка ввода')
c = str('55.0')
print(c)
