#Задание 2. Лестница

number = int(input("Введите число: "))

for i in range(1, number + 1):
    for j in range(i):
        print(i, end="\t")
    print()