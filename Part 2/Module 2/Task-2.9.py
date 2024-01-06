#Задание 9. Обратный анализ чётных чисел

numbers = input("Введите список чисел через пробел: ").split()
numbers = [int(x) for x in numbers]

print("Чётные в обратном порядке:")
for num in reversed(numbers):
    if num % 2 == 0:
        print(num, end=" ")
