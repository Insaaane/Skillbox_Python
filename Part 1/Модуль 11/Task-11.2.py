#Задача 2. Грубая математика

import math

n = int(input('Введите кол-во чисел: '))

for i in range(n):
    num = float(input('Введите число: '))
    if num > 0:
        num = math.ceil(num)
        res = math.log(num)
        print(f'x = {num} log(x) = {res}')
    else:
        num = math.floor(num)
        res = math.exp(num)
        print(f'x = {num} exp(x) = {res}')
