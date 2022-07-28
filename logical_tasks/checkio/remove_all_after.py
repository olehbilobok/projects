"""Not all of the elements are important. What you need to do here is to remove all of the elements after the given
one from list."""

def remove_all_after(items: list, border: int):
    final = []
    if border in items:
        for x in items:
            final.append(x)
            if x == border:
                break
        return final
    return items


print(remove_all_after([1, 2, 3, 4, 5], 3))
print(remove_all_after([1, 1, 2, 2, 3, 3], 2))
print(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2))
print(remove_all_after([1, 1, 5, 6, 7], 2))
print(remove_all_after([], 0))
print(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7))
