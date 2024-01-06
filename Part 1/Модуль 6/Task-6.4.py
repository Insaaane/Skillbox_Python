#Задача 4. Поставьте оценку!

rate = int(input("Введите число: "))
positive_rate = 0
negative_rate = 0

while rate != 0:
    if rate > 0:
        positive_rate+=1
    else:
        negative_rate+=1
    rate = int(input("Введите число: "))

print("Кол-во положительных чисел: " + str(positive_rate))
print("Кол-во отрицательных чисел: " + str(negative_rate))
