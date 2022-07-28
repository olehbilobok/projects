'''Напишите функцию, которая принимает список, и число. Функция должна разбить список на N кусков, переданных в функцию
в качестве втрого аргумента. Выполнить проверки по здравому смыслу (например, нет смысла пытаться разбить список
из 3 элементов на 4 элемента)'''


def cut_list(data, n):
    final = []
    count = 0

    for x in data:

        count += 1

        if count == n:
            final.append(data[data.index(x):])
            break

        final.append([x])

    return final


print(cut_list(['ferrari', 'lamborghini', 'ford', 'jeep', 'audi'], 3))