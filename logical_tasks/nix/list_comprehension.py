'''Дан список из строк. Создайте однострочное решение (при помощи list comprehension),
которое приведёт к верхнему регистру все строки, содержащие слово 'price')'''


def new_list(txt):
    return [x.upper() for x in txt if x == 'price']


print(new_list(['name', 'price', 'car', 'apple', 'price']))
