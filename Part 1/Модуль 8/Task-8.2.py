#Задача 2. Долги

numbers = int(input("Введите количество должников: "))
summ = 0

for i in range(0, numbers, 5):
    print("Должник с номером", i)
    summ += int(input("Сколько должны? "))
    print()

print("Общая сумма долга:", summ)