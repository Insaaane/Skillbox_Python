#Задача 2. Функция максимума

def maximum_of_two(first, second):
    if first > second:
        return first
    return second

def maximum_of_three(first, second, third):
    return maximum_of_two(maximum_of_two(first, second), third)

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

print(maximum_of_two(first_number, second_number), maximum_of_three(first_number, second_number, third_number))