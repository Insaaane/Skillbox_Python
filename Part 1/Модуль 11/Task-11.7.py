#Задача 7. За что?

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

result = (num1 + num2 + abs(num1 - num2)) / 2

print("Наибольшее число:", result)
