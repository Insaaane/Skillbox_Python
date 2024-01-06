#Задание 9. Анализ комментариев

def count_uppercase_lowercase(text):
    upper = len([char for char in text if char.isupper()])
    lower = len([char for char in text if char.islower()])
    return upper, lower


text_input = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text_input)

print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
