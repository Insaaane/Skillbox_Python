#Задача 1. Должники

print("Введите 10 чисел:")
count = 0
for i in range(10):
    num = int(input())
    if num > 0 and num % 2 == 0:
        count += 1
print("Количество четных положительных чисел:", count)
