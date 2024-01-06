#Задание 8. Симметричная последовательность

def get_missing_numbers(source):
    for i in range(len(source)):
        numbers = source[i:]
        if numbers == numbers[::-1]:
            return list(reversed(source[:i]))


count = int(input('Количество чисел: '))
list_of_numbers = []

for x in range(count):
    number = int(input('Число: '))
    list_of_numbers.append(number)

need_to_add = get_missing_numbers(list_of_numbers)

print('Последовательность:', list_of_numbers)
print('Нужно приписать чисел:', len(need_to_add))
print('Сами числа:', need_to_add)
