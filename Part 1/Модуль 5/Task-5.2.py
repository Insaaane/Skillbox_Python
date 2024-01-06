#Задача 2. Функция

def function(x):
    if x > 0:
        return x - 12
    elif x == 0:
        return 5
    else:
        return x**2

result = function(int(input("Введите икс: ")))

print("Игрек равен " + str(result))