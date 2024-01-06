#Задача 6. Новоселье

cost = int(input("Стоимость квартиры: "))
square = int(input("Площадь квартиры: "))

if ((cost < 10_000_000 and square >= 100) or
    (cost < 7_000_000 and square >= 80)):
    print("Берём эту квартиру")
else:
    print("Такая квартира не нужна")
