#Задание 7. Метод бутерброда

input_text = input("Введите зашифрованное сообщение: ")

first_text = ""
second_text = ""

for index_char in range(1, len(input_text) + 1, 2):
    first_text += input_text[index_char-1]

for index_char in range(2, len(input_text) + 1, 2):
    second_text = input_text[index_char-1] + second_text

print("Расшифрованное сообщение:", first_text + second_text)