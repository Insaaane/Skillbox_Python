#Задание 6. Коровы

input_text = input("Введите последовательность: ")

result_liters = 0
for stall in range(1, 11):
    if input_text[stall-1] == "b":
        result_liters += 2 * stall

print("Всего молока за день: ", result_liters)