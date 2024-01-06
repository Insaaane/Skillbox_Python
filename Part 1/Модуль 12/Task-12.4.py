def reverse_number(number):
    while number % 10 == 0:
        number /= 10
    reversed_number = str(int(number))[::-1]
    print(f"Число наоборот: {reversed_number}")


while True:
    number = int(input("Введите число: "))

    if number == 0:
        print("Программа завершена!")
        break

    reverse_number(number)
