#Задание 2. Генерация

n = int(input("Введите длину списка: "))

result = [1 if num % 2 == 0 else num % 5 for num in range(n)]

print(f"Результат: {result}")