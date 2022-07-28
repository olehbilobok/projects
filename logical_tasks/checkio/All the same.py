"""In this mission you should check if all elements in the given list are equal."""

def all_the_same(elements):
    if elements:
        for x in elements:

            if elements.count(x) == len(elements):
                return True
            return False
    return True


print(all_the_same([1, 1, 1, 2]))
print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))
print(all_the_same(['a', 'a', 'a']))
print(all_the_same([]))
print(all_the_same([1]))
