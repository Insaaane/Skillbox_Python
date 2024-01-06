#Задание 8. Сортировка

list_of_numbers = []
count = int(input('Кол-во чисел: '))

for i in range(count):
    list_of_numbers.append(int(input('Введите число: ')))

print('Изначальный список:', list_of_numbers)
print('Отсортированный список:', sorted(list_of_numbers))