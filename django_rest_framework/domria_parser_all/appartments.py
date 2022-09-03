import requests
from cities import city_ids


photo_host = 'https://cdn.riastatic.com/photos/'
url_appartments = 'http://127.0.0.1:8000/api/v1/appartments/'
url_owners = 'http://127.0.0.1:8000/api/v1/owners/'


def get_appartments_ids():
    appartments_ids = []
    for id in city_ids:
        for operation in [1, 3]:
            page = 0
            while True:
                appartments_data = requests.get(
                    f"https://dom.ria.com/node/searchEngine/v2/?category=1&realty_type=2&operation={operation}&\
                    state_id={id}&city_id={id}&in_radius=0&with_newbuilds=0&price_cur=1&wo_dupl=0&\
                    inspected=0&sort=created_at&period=0&notFirstFloor=0&notLastFloor=0&with_map=0&photos_count_from=0&\
                    firstIteraction=false&type=list&client=searchV2&limit=20&page={page}&\
                    ch=209_f_0,209_t_0,235_f_0,235_t_0,246_244").json()

                print(f'[INFO] parsing page number: {page}')
                print(appartments_data)

                # if len(appartments_data['items']) == 0:
                #     break
                if len(appartments_data['items']) != 0:
                    appartments_ids.extend(appartments_data.get('items'))

                if page == 0:
                    break
                page += 1


    return appartments_ids


def get_data(appartments_ids):
    appartments_info = []

    for appart in appartments_ids:

        appartments_json = requests.get(
            f"https://dom.ria.com/node/searchEngine/v2/view/realty/{appart}?lang_id=4").json()
        try:
            name = appartments_json.get('user').get('name')
            price = int((appartments_json.get('priceArr').get('3')).replace(' ', ''))
        except:
            name = 'NoName'
            price = 'NoPrice'
        appartments_info.append(
            {
                'appartments': {
                    'id': appartments_json.get('realty_id'),
                    'operation_type': appartments_json.get('advert_type_id'),
                    'city': appartments_json.get('city_id'),
                    'district_name': appartments_json.get('district_name_uk'),
                    'street_name': appartments_json.get('street_name_uk') or appartments_json.get('street_name'),
                    'square_meters': appartments_json.get('total_square_meters'),
                    'rooms_count': appartments_json.get('rooms_count'),
                    'floor': appartments_json.get('floor'),
                    'total_price': price,
                    'created_at': appartments_json.get('created_at'),
                    'user': appartments_json.get('user_id'),
                    'photo': appartments_json.get('main_photo')
                    },
                'owners': {
                    'id': appartments_json.get('user_id'),
                    'name': name

                    }
            }
        )
    print(len(appartments_info))
    return appartments_info


def post_data(url, data):
    requests.post(url, data=data)


def head(url):
    return requests.head(url)


def main():

    appartments_ids = get_appartments_ids()
    appartments_info = get_data(appartments_ids)

    for appartments_data in appartments_info:

        owners = appartments_data.get('owners')
        appartments = appartments_data.get('appartments')

        if head(url_owners + str(owners.get('id')) + '/').status_code == 404:
            post_data(url_owners, owners)

        if head(url_appartments + str(appartments.get('id')) + '/').status_code == 404:
            post_data(url_appartments, appartments)


if __name__ == "__main__":
    main()
