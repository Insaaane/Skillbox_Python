#Задача 2. Счастливое число

import random


out_file = open('out_file.txt', 'w')
max_sum = 777

try:
    with out_file:
        while max_sum > 0:
            input_number = int(input('Введите число: '))

            if random.randint(1, 13) == 1:
                raise Exception

            max_sum -= input_number
            out_file.write(f'{str(input_number)}\n')

except Exception:
    print('Вас постигла неудача!')
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')