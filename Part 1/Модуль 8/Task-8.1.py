#Задача 1. Космическая еда

buckwheat = 100
months = 100 // 4

for i in range(1, months+1):
    buckwheat -= 4
    print("Месяцев прошло:", i)
    print("Гречки осталось:", buckwheat, "кг")
    print()