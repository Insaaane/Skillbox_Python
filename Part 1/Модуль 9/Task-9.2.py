#Задание 2. Кривой мессенджер

input_text = input("Введите текст: ")
char_counter = 0

for char in input_text:
    char_counter += 1
    if char == '*':
        print("Символ «*» стоит на позиции " + str(char_counter))