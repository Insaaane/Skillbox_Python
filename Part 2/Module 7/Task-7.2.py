#Задача 2. Универсальная программа

def is_prime(number):
    if number == 1 or number == 0:
        return False

    for divider in range(2, round(number**0.5+1)):
        if number % divider == 0:
            return False

    return True


def crypto(obj):
    result = []
    for index, item in enumerate(obj):
        if is_prime(index):
            result.append(item)

    return result


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(crypto('О Дивный Новый мир!'))