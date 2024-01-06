#Задача 5. Отрезок

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

count = 0
summ = 0

for i in range(a, b+1):
    if i % 3 == 0:
        count += 1
        summ += i

print("Среднее арифметическое всех чисел из отрезка, кратных числу 3, равно: ", summ / count)
