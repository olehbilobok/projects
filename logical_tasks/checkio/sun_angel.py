"""Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun
rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith,
which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return -
"I don't see the sun!"."""


def sun_angle(time: str):
    data = []
    angel_hour = 15
    angel_minute = 0.25

    for x in time.split(':'):
        data.append(int(x))

    if data[0] < 6 or data[0] >= 18 and data[1] > 0:
        return "I don't see the sun"

    return (data[0] - 6) * angel_hour + data[1] * angel_minute


print(sun_angle("07:00"))
print(sun_angle("12:15"))
print(sun_angle("01:23"))
