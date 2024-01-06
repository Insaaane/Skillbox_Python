#Задание 2. Самое длинное слово

message = input('Введите строку: ').split()
longest_message = max(message, key=len)
print(f'Самое длинное слово: «{longest_message}»')
print(f'Длина этого слова: {len(longest_message)}')
