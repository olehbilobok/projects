"""You have to split a given array into two arrays. If it has an odd amount of elements,
then the first array should have more elements. If it has no elements, then two empty arrays should be returned."""


import math

def split_list(items):
    if items:
        middle_index = math.ceil(len(items) / 2)
        first_part = items[0:middle_index]
        second_part = items[middle_index:]
        return [first_part, second_part]

    return [[], []]


print(split_list([1, 1, 1, 1, 1]))
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))
