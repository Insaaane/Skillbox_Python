#Задание 1. Страшный код

main_list = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

main_list.extend(b)
count_five = main_list.count(5)
print(f"Количество цифр 5 при первом объединении: {count_five}")

while 5 in main_list:
    main_list.remove(5)

main_list.extend(c)
count_three = main_list.count(3)
print(f"Количество цифр 3 при втором объединении: {count_three}")
print(f"Итоговый список: {main_list}")
