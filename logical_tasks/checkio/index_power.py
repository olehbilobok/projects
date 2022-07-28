"""You are given an array with positive numbers and a number N. You should find the N-th power of the element
in the array with the index N. If N is outside of the array, then return -1"""


def index_power(array, n):

    for x in range(len(array)):

        if n == x:
            return array[x] ** n
    return -1


print(index_power([1, 2, 43, 5], 3))
print(index_power([1, 3, 10, 100], 3))
print(index_power([0, 1], 0))
print(index_power([1, 2], 3))