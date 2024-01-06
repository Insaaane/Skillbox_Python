#Задача 7. Сумма ряда

n = int(input("Введите N: "))
summ = 0

for i in range(n):
    summ += (-1)**i * (1/2)**i

print(f"Ответ: {summ}")