"""Создать функцию, которая принимает на вход два списка: первый — список, который нужно очистить от определённых
значений, второй — список тех значений, от которых нужно очистить.
Например, list1 = [1, 2, 3, 4, 5], list2 = [1, 3, 4], функция должна вернуть [2, 5] """


def list_odering(first_list, second_list):


    return [x for x in first_list if x not in second_list]


print(list_odering([1, 2, 3, 4, 5], [1, 3, 4]))
