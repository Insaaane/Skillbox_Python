#Задача 6. Замечательные числа

for i in range(10, 100):
    if i == (i // 10) * (i % 10) * 3:
        print(i)