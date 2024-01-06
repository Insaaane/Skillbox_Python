def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total


def max_digit(number):
    max_digit = max(str(number))
    return int(max_digit)


def min_digit(number):
    min_digit = min(str(number))
    return int(min_digit)


while True:
    user_input = input("Введите число (или 'q' для выхода): ")

    if user_input.lower() == 'q':
        break

    number = int(user_input)
    action = input("Выберите действие ('сумма', 'максимум' или 'минимум'): ")

    if action == 'сумма':
        result = sum_of_digits(number)
    elif action == 'максимум':
        result = max_digit(number)
    else:
        result = min_digit(number)

    print(f"Результат: {result}")
    