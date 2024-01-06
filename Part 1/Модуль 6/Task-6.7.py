#Задача 7. Игра «Угадай число»

hidden_number = int(input("Загадайте число: "))
number = int(input("Введите число: "))
number_of_attempts = 1

while hidden_number != number:
    if number < hidden_number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif number > hidden_number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")

    number = int(input("Введите число: "))
    number_of_attempts += 1

print("Вы угадали! Число попыток: " + str(number_of_attempts))