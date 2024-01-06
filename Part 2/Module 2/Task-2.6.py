#Задание 6. Бегущие цифры

list_of_numbers = input("Введите изначальный список: ").split()
offset_count = int(input("Введите кол-во позиций для сдвига: "))

result_list = list_of_numbers[-offset_count:] + list_of_numbers[:-offset_count]

print("Сдвинутый список:", " ".join(result_list))
