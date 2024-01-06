#Задача 3. Факториал

number = int(input("Факториал числа: "))
factorial = 1;
for i in range(1, number+1):
    factorial *= i;

print("Факториал числа", number, "равен:", factorial)
