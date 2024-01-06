#Задача 1. Калькулятор опыта

level = 1

current_xp = int(input("Введите количество опыта: "))

if current_xp >= 5000:
    level += 3
elif current_xp >= 2500:
    level += 2
elif current_xp >= 1000:
    level += 1

print(level)