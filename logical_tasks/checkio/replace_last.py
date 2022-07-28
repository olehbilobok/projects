"""In a given list the last element should become the first one. An empty list or list with only one element
should stay the same"""

def replace_last(line):
    if line:
        final = []
        final.append(line.pop())
        for x in line:
            final.append(x)

        return final
    return []

print(replace_last([2, 3, 4, 1]))
print(replace_last([1, 2, 3, 4]))
print(replace_last([1]))
print(replace_last([]))
