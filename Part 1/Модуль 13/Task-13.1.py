#Задача 1. Урок информатики 2

input_number = float(input("Введите число: "))
counter_pow = 0

while input_number > 10:
    input_number /= 10
    counter_pow +=1

while 0 < input_number < 1:
    input_number *= 10
    counter_pow -= 1

print("Формат плавающей точки: x =", round(input_number, 10), "* 10 **", counter_pow)