#Задача 5. Вася хочет выигрывать

numbers1, numbers2, numbers3 = map(int, input("Введите три числа (через пробел): ").split())

if numbers1 == numbers2 == numbers3:
    print("(3) Все числа совпадают")
elif numbers1 == numbers2 or numbers2 == numbers3 or numbers1 == numbers3:
    print("(2) Два числа совпадают")
else:
    print("(0) Все числа разные")