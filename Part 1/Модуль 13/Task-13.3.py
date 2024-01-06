#Задача 3. Число наоборот 2

def reverse_number(number):
    return int(str(number)[::-1])

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

num1_reversed = reverse_number(num1)
num2_reversed = reverse_number(num2)

print("\nПервое число наоборот:", num1_reversed)
print("Второе число наоборот:", num2_reversed)

num_sum = num1_reversed + num2_reversed

print("Сумма:", num_sum)
print("\nСумма наоборот:", num1 + num2)