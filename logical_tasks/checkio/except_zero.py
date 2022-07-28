"""Sort the numbers in an array. But the position of zeros should not be changed"""
def except_zero(items: list):

    sorted_list = []
    for x in range(len(items)):
        if items[x] != 0:
            sorted_list.append(items[x])
            sorted_list.sort()
    new_list = sorted_list.copy()

    for x in range(len(items)):
        if items[x] == 0:
            new_list.insert(x, items[x])

    return new_list


print(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]))
print(except_zero([0, 2, 3, 1, 0, 4, 5]))
print(except_zero([0, 0, 0, 1, 0]))
print(except_zero([4, 5, 3, 1, 1]))
print(except_zero([0, 0]))
