#Задание 4. Гистограмма частоты — 2

input_text = input("Введите текст: ")
original_dict = dict()
inverted_dict = dict()

for char in input_text:
    if char in original_dict:
        original_dict[char] += 1
    else:
        original_dict[char] = 1

print("Оригинальный словарь частот: ")
for char in original_dict:
    print(char, ":", original_dict[char])


for char in original_dict.keys():
    if original_dict[char] in inverted_dict:
        inverted_dict[original_dict[char]].append(char)
    else:
        inverted_dict[original_dict[char]] = [char]

print("Инвертированный словарь частот:")
for i in inverted_dict:
    print(i, ":", inverted_dict[i])
