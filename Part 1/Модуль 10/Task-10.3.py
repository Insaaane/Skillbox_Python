#Задание 3. Рамка

rows = int(input("Кол-во строк: "))
columns = int(input("Кол-во столбцов: "))

for y in range(columns):
    for x in range(rows):
        if x == 0 or x == rows-1:
            print("|", end="")
        elif y == 0 or y == columns-1:
            print("-", end="")
        else:
            print(" ", end="")
    print()