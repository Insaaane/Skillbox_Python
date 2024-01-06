#Задание 5. Великий и могучий

text_input = input("Введите текст: ").split()
max_lenght = 0

for word in text_input:
    current_lenght = len(word)
    if word[-1] == ".":
        current_lenght -= 1

    max_lenght = max(current_lenght, max_lenght)

print("Самое длинное слово, букв: ", max_lenght)