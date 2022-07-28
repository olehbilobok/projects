import requests
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import execute_values
from psql_tables import tables

photo_host = 'https://cdn.riastatic.com/photos/'

city_id_data = {
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

data_for_psql = [(k, v) for k, v in city_id_data.items()]


def get_appart_id_data(data):
    appart_id_data = []

    page = 0
    while True:
        appartments = requests.get(
            f"https://dom.ria.com/node/searchEngine/v2/?category=1&realty_type=2&operation={data['rent or buy']}&state_id={data['city_id']}&city_id={data['city_id']}&in_radius=0&with_newbuilds=0&price_cur=1&wo_dupl=0&inspected=0&sort=inspected_sort&period=0&notFirstFloor=0&notLastFloor=0&with_map=0&photos_count_from=0&firstIteraction=false&type=list&client=searchV2&limit=20&page={page}&ch=209_f_{data['number_of_rooms_from']},209_t_{data['number_of_rooms_to']},235_f_{data['price_from']},235_t_{data['price_to']},246_244").json()

        print(f'[INFO] parsing page number: {page}')

        if len(appartments['items']) == 0:
            break
        page += 1

        if len(appartments['items']) != 0:
            appart_id_data.extend(appartments['items'])

    print(len(appart_id_data))
    print(appart_id_data)
    return appart_id_data


def get_appart_links_data(appart_id_data):
    appart_links_data = []

    for appart in appart_id_data:
        appart_links = f"https://dom.ria.com/node/searchEngine/v2/view/realty/{appart}?lang_id=4"
        print(appart_links)
        appart_links_data.extend([appart_links])

    print(appart_links_data)
    return appart_links_data


def get_appart_json(appart_links_data):
    appart_json_data = []

    for link in appart_links_data:
        appart_json_data.extend([requests.get(link).json()])

    print(len(appart_json_data))
    return appart_json_data


def get_appart_info(appart_json_data, data):
    appart_info_data = []

    for item in appart_json_data:
        appartment_id = item.get('realty_id')
        city_id = item.get('city_id')
        district_name = item.get('district_name_uk')
        street_name = item.get('street_name_uk') or item.get('street_name')
        square_meters = item.get('total_square_meters')
        rooms_count = item.get('rooms_count')
        floor = item.get('floor')
        total_price = item.get('priceArr').get('3')
        created_at = item.get('created_at')
        user_id = item.get('user_id')
        photo = item.get('main_photo')
        operation_type = data['rent or buy']

        appart_info_data.append(
            [appartment_id, operation_type, city_id, district_name, street_name, square_meters, rooms_count, floor,
             total_price, created_at, user_id, photo])

    print(appart_info_data)
    return appart_info_data


def get_connection():
    connection = psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='43Alinod1142a',
        database='domriadb'
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return connection.cursor()


cursor = get_connection()


def create_table(table, rows):
    cursor.execute(f'CREATE TABLE {table}({rows})')


def insert_data(table, data):
    execute_values(cursor, f'INSERT INTO {table} VALUES %s', data)


def drop_table(table):
    cursor.execute(f'DROP TABLE IF EXISTS {table} CASCADE')


def main():
    print("Choose the city_id by using the chart below: ")
    print("Enter zero in the fields (except required) if you don't want to apply filters")

    for cityid in city_id_data.items():
        print(cityid)

    data = {
        'city_id': int(input('Enter city_id here(required field*): ')),
        'rent or buy': input("Enter 'buy' if you want to buy appartment, enter 'rent' if you want to rent: "),
        'number_of_rooms_from': int(input('Enter number of rooms from: ')),
        'number_of_rooms_to': int(input('Enter number of rooms to: ')),
        'price_from': int(input('Enter price_from: ')),
        'price_to': int(input('Enter price to: '))
    }

    if data['rent or buy'] == 'buy':
        data['rent or buy'] = 1
    elif data['rent or buy'] == 'rent':
        data['rent or buy'] = 3

    appart_id = get_appart_id_data(data)
    appart_links = get_appart_links_data(appart_id)
    appart_json = get_appart_json(appart_links)
    appart_info = get_appart_info(appart_json, data)

    for table in tables:
        drop_table(table['name'])

    for table in tables:
        create_table(table['name'], table['rows'])
        if table['name'] == 'cities':
            insert_data(table['name'], data_for_psql)
        elif table['name'] == 'appartments':
            insert_data(table['name'], appart_info)

    print('[INFO] DATA HAS BEEN SAVED SUCCESSFULLY')


if __name__ == "__main__":
    main()
