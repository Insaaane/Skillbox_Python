#Задача 4. Недоделка 2

def count_number(number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count

def change_number(number):
    number = int(str(number)[-1] + str(number)[1:-1] + str(number)[0])
    return number

def main():
    first_n = int(input("Введите первое число: "))
    if count_number(first_n) < 3:
        print("В первом числе меньше трёх цифр")
    else:
        first_n = change_number(first_n)
        print(f"Изменённое первое число: {first_n}")
    second_n = int(input("Введите второе число: "))
    if count_number(second_n) < 4:
        print("Во втором числе меньше четырёх цифр")
    else:
        second_n = change_number(second_n)
        print(f"Изменённое первое число: {second_n}")
    print(f"Сумма чисел: {first_n + second_n}")

main()