#Задание 5. Пароль

while True:
    password = input("Придумайте пароль: ")
    capitalized_letter_count = len([char for char in password if char.isupper()])
    digit_count = len([char for char in password if char.isdigit()])

    if len(password) >= 8 and capitalized_letter_count > 0 and digit_count >= 3:
        print("Это надёжный пароль.")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
