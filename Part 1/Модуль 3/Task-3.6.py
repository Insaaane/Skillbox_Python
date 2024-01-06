#Задача 6. Проверяем бухгалтера

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

summ = number_1 % 100 + number_2 % 100

print('Сумма: ' + str(summ))
