#Задача 2. Финансовый отчёт

number_1 = int(input('Доходы за первый квартал: '))
number_2 = int(input('Доходы за второй квартал: '))
number_3 = int(input('Доходы за третий квартал: '))
number_4 = int(input('Доходы за четвертый квартал: '))

res = (number_1 + number_2) / (number_3 + number_4)
print(res)
