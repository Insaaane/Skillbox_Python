#Задача 7. Хватит ли зарплаты

hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
meal = int(input('Введите траты на еду: '))

salary = 200 * hours / 8 + hours

if salary <= meal + credit:
    print('Часов не хватает. Придётся работать больше!')
else:
    print('Часов хватает. Можно отдохнуть')