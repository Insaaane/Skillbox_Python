#Задание 1. Генерация списка

def get_odd_list(n: int):
    return list(range(1, n + 1, 2))


num = int(input('Введите число N: '))
print('Список из нечётных чисел от одного до N:', get_odd_list(num))