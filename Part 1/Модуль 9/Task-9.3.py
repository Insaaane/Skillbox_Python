#Задание 3. Театр

rows = int(input("Введите кол-во рядов: "))
seats = int(input("Введите кол-во сидений в ряде: "))
distance = int(input("Введите кол-во метров между рядами: "))

print("\nСцена\n")

for row in range(rows):
    print("=" * seats + " " + "*" * distance + " " + "=" * seats)