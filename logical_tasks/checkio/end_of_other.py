from ordered_set import OrderedSet
def checkio(words_set):
    l = list(words_set)
    if len(l) > 1:
        for x in range(len(l)):
            if (l[x].endswith(l[x+1])) or (l[x+1].endswith(l[x])):
                print(l)
                return True
            return False
    return False

print(checkio({"lo","hello", "he"}))
print(checkio({"hello", "lo", "he"}))
print(checkio({"hello", "la", "hellow", "cow"}))
print(checkio({"walk", "duckwalk"}))
print(checkio({"one"}))
print(checkio({"helicopter", "li", "he"}))