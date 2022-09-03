import requests


url_cities = 'http://127.0.0.1:8000/api/v1/cities/'

city_ids = {
    1: 'Вінниця',
    2: 'Житомир',
    3: 'Тернопіль',
    4: 'Хмельницький',
    5: 'Львів',
    6: 'Чернігів',
    7: 'Харків',
    8: 'Суми',
    9: 'Рівне',
    10: 'Київ',
    11: 'Дніпро',
    12: 'Одеса',
    14: 'Запоріжжя',
    15: 'Івано-Франківськ',
    16: 'Кропивницький',
    18: 'Луцьк',
    19: 'Миколаїв',
    20: 'Полтава',
    22: 'Ужгород',
    23: 'Херсон',
    24: 'Черкаси',
    25: 'Чернівці'
}


def main():

    for id, city in city_ids.items():
        city_request = requests.post(url_cities, data={
            'id': id,
            'city_name': city
            }
                      )
        print(f'[INFO] Status code is {city_request.status_code}')


if __name__ == '__main__':
    main()


