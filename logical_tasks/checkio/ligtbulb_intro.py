"""There is a light bulb, which by default is off, and a button, by pressing which the light bulb switches its state.
This means that if the light bulb is off and the button is pressed, the light turns on, and if you press it again,
it turns off. The function input is an array of datetime objects - this is the date and time of pressing the button.
Your task is to determine how long the light bulb has been turned on."""


from datetime import datetime, timedelta
from typing import List


def sum_light(els: List[datetime]):
    data = []
    final = []

    for x in range(len(els) - 1):
        data.append(abs(els[x] - els[x + 1]))

    for x in range(len(data)):
        if x % 2 == 0:
            final.append(data[x])
    return sum(final, timedelta()).total_seconds()


print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
]))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
]))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
    datetime(2015, 1, 12, 11, 10, 10),
    datetime(2015, 1, 12, 12, 10, 10),
]))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 1),
]))
print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 13, 11, 0, 0),
]))
