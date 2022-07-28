"""This is the second mission in the lightbulb series. I will try to make each following task slightly more complex.
You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit.
Now let's add one more parameter - the counting start time. This means that the light continues to turn on and off as
before. But now, as a result of the function, I want not only to know how long there was light in the room, but how
long the room was lit, starting from a certain moment. One more argument is added – start_watching , and if it’s not
passed, we count as in the previous version of the program for the entire period."""


from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None):
    data = []
    data.append(start_watching)
    for x in els:
        if x not in data:
            data.append(x)
    new_data = sorted(data)
    index = new_data.index(start_watching)
    if new_data:
        for x in range(index, len(new_data) - 1):
            return (new_data[x + 1] - new_data[x]).total_seconds()
    return 0


print(sum_light([datetime(2015, 1, 12, 10, 0, 0),
                 datetime(2015, 1, 12, 10, 0, 10), ],
                datetime(2015, 1, 12, 10, 0, 5), ))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10), ],
    datetime(2015, 1, 12, 11, 0, 0), ))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10), ],
    datetime(2015, 1, 12, 11, 0, 10), ))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10), ],
    datetime(2015, 1, 12, 10, 10, 0), ))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
    datetime(2015, 1, 12, 11, 10, 11),
    datetime(2015, 1, 12, 12, 10, 11), ],
    datetime(2015, 1, 12, 12, 10, 11), ))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
    datetime(2015, 1, 12, 11, 10, 11),
    datetime(2015, 1, 12, 12, 10, 11), ],
    datetime(2015, 1, 12, 12, 9, 11), ))
