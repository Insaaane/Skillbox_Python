#Задача 4. Калькулятор скидки

sum1 = int(input('Введите первую сумму: '))
sum2 = int(input('Введите вторую сумму: '))
sum3 = int(input('Введите третью сумму: '))

summ = sum1 + sum2 + sum3
if summ > 10000:
    summ *= 0.9
print(summ)