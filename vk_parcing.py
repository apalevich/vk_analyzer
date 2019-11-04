import requests
from vk_token import TOKEN

query_url = 'https://api.vk.com/method/'
query_method = 'wall.get'
version = 5.103
query_parameters = {'access_token': TOKEN,
                    'v': version,
                    'count': 100}
# page = 'id1524756'


def update_params(page=None):
    if not page:
        page = input('Введите идентификатор или домен страницы (символы после последнего знака "/")')
    if page.startswith('id') and page[2:].isdigit():
        query_parameters['owner_id'] = int(page[2:])
    elif page.startswith('club') and page[4:].isdigit():
        query_parameters['owner_id'] = int('-' + page[4:])
    else:
        query_parameters['domain'] = page
    return False


def get_posts():
    # TODO: УБРАТЬ СВОЙ АРГУМЕНТ
    update_params(page='id1524756')
    response = requests.get(query_url + query_method, params=query_parameters)
    return response.json()['response']['items']


data = get_posts()

data_sorted = sorted(data, key=lambda p: p['likes']['count'], reverse=True)

print(data_sorted)