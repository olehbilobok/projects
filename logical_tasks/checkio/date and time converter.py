import datetime
import re


def date_time(time: str):
    data = re.split(r"[.:' ']", time)
    result = tuple(data)
    (day, month, year, hour, minutes) = result
    final = datetime.datetime(int(year), int(month), int(day), int(hour), int(minutes))
    x = final.strftime("%d"), final.strftime("%B"), final.strftime("%Y") + ' ' + "year", final.strftime("%H") + \
        ' ' + "hours", final.strftime("%M") + ' ' + "minutes"
    return ' '.join(x)


print(date_time("01.01.2000 00:00"))
print(date_time("09.05.1945 06:30"))
print(date_time("20.11.1990 03:55"))
