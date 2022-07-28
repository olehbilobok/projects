'''Дан список из строк. Используя join, соедините строки так, чтобы они были разделены через запятую.
На выходе должна получиться строка в виде "my_string1,my_string2,my_string3"'''


def new_list(data):
    return ','.join(data)

print(new_list(['my_string1', 'my_string2', 'my_string3']))