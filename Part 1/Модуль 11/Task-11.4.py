#Задача 4. Первая цифра

x = float(input("Введите положительное действительное число X: "))

fractional_part = x - int(x)
first_digit = int(fractional_part * 10)

print("Первая цифра после десятичной точки:", first_digit)