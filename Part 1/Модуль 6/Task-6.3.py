#Задача 3. Слишком большие числа

number = int(input("Введите своё число: "))
length_number = 0

while number != 0:
    length_number+=1
    number//=10

print("Длина числа: " + str(length_number))