#Задача 3. Глубокое копирование

import copy


def get_new_site(phone):
    new_site = copy.deepcopy(site)
    new_site['html']['head']['title'] = new_site['html']['head']['title'].format(phone)
    new_site['html']['body']['h2'] = new_site['html']['body']['h2'].format(phone)
    return new_site


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

count = int(input('Сколько сайтов: '))
sites = dict()

for i in range(count):
    phone_name = input('Введите название продукта для нового сайта: ')
    sites[phone_name] = get_new_site(phone_name)
    for phone_name, site in sites.items():
        print(f'Сайт для {phone_name}:')
        print(f'{site}\n')
