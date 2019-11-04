import requests
from token import TOKEN

query_url = 'https://api.vk.com/method/'
query_method = 'wall.get'
version = 5.103
query_parameters = {'access_token': TOKEN,
                    'v': version}

page = input('Введите идентификатор или домен страницы (символы после последнего знака "/")')
if page.startswith('id') and page[2:].isdigit():
    query_parameters['owner_id'] = int(page[2:])
    # pass # owner_id
elif page.startswith('club') and page[4:].isdigit():
    query_parameters['owner_id'] = int('-' + page[4:])
else:
    query_parameters['domain'] = page