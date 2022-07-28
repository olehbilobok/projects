"""Your mission is to sort the list by the frequency of numbers included in it. If a few numbers have an equal
frequency - they should be sorted according to their natural order. For example:
 [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]"""


def frequency_sorting(numbers):

    return sorted(sorted(numbers), key=numbers.count, reverse=True)


print(frequency_sorting([1, 2, 3, 4, 5]))
print(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]))
print(frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]))
