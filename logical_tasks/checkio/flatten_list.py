"""There is a list which contains integers or other nested lists which may contain yet more lists and integers which
then… you get the idea. You should put all of the integer values into one flat list. The order should be as it was in
the original list with string representation from left to right"""
import re


def flat_list(array):
    final = []

    into_str = ''.join(str(array))
    res = re.split('[],[]', into_str)
    for x in res:
        final.append(x.strip())
    remove_space = ' '.join(final).split()
    result = list(map(int, remove_space))
    return result


print(flat_list([1, 2, 3]))
print(flat_list([1, [2, 2, 2], 4]))
print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
print(flat_list([-1, [1, [-2], 1], -1]))
