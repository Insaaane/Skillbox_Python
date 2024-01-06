#Задача 1. Кубы чисел

number = int(input("Число, до которого нужно посчитать третью степень "))

current_number = 1

while current_number < number:
    print("Для числа " + str(current_number) + " третья степень равна " + str(current_number**3))
    current_number += 1