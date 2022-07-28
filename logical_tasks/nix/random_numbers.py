import random


def random_list():

    data = [random.randint(0, 1000) for _ in range(0, 1000)]

    if 777 in data:
        if data.index(777) <= 100:
            return "Dobre"

    return "Error"


print(random_list())
