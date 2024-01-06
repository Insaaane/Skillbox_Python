#Задание 5. Наибольшая сумма цифр

n = int(input("Кол-во чисел: "))

result_number = -1
result_sum = -1

for i in range(n):
    number = input("Введите число: ")
    current_sum = 0
    for j in number:
        current_sum += int(j)
    if result_sum < current_sum:
        result_sum = current_sum
        result_number = number

print("Самая большая сумма цифр", result_sum, "у числа", result_number)