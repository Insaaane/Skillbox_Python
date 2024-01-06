def count_letters():
    text = input("Введите текст: ").lower()
    digit_to_count = input("Какую цифру ищем? ")
    letter_to_count = input("Какую букву ищем? ")

    count_digit = text.count(digit_to_count)
    count_letter = text.count(letter_to_count.lower())

    print(f"Количество цифр {digit_to_count}: {count_digit}")
    print(f"Количество букв {letter_to_count}: {count_letter}")


count_letters()
