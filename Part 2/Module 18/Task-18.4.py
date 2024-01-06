#Задача 4. Телефонные номера

import re

phone_numbers = ['9999999999', '999999-999', '99999x9999', '8912345678']

for number in phone_numbers:
    if re.match(r'^[89]\d{9}$', number):
        print(f'{number}: всё в порядке')
    else:
        print(f'{number}: не подходит')
        