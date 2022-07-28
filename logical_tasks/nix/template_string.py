"""Напишите template строки, который можно будет многократно переиспользовать,
 вставляя в него имя и фамилию человека. Используйте метод строки format"""

value1 = input("Please, enter your name: ")
value2 = input("Please, enter your surname: ")
template = "Hello {} {}, that's great you are on your way of learning Python"
print(template.format(value1, value2))