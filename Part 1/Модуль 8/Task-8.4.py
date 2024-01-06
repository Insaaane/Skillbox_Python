#Задача 4. Среднее на отрезке

a = int(input("Введите начальное число a: "))
b = int(input("Введите конечное число b: "))
c = int(input("Введите число c: "))

summ = 0
count = 0

for number in range(a, b + 1):
    if number % c == 0:
        summ += number
        count += 1

if count == 0:
    print("В заданном интервале нет чисел, кратных", c)
else:
    average = summ / count
    print("Среднее арифметическое всех чисел в интервале [a, b], кратных", c, "равно", average)
