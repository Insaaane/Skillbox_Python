#Задача 2. Посчитай чужую зарплату...

print("Введите зарплату за каждый из 12 месяцев: ")
summ = 0
for i in range(12):
    summ += int(input())
print("Средняя зарплата за год:", summ / 12)

