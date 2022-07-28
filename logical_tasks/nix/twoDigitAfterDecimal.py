'''Напишите функцию, которая будет преобразовывать цену к формату, отображающему до двух знаков после точки'''


def two_digit(n):
    final = []
    for x in n:
        string_ = str(x)
        if string_.endswith('0'):

            for y in range(len(string_)):

                if string_[y] == '.':
                    index = string_.index(string_[y])
                    final.append(int(string_[0:index]))
        else:
            final.append(round(x, 2))

    return final


print(two_digit([22.32131, 58.60125, 34.0]))
