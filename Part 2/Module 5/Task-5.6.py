#Задание 6. Сжатие

string = input("Введите строку: ")

result = []
count = 1

for letter in range(len(string)):
    if letter == len(string)-1:
        result.append(string[letter] + str(count))
    elif string[letter] == string[letter+1]:
        count += 1
    else:
        result.append(string[letter] + str(count))
        count = 1

result = ''.join(result)
print(f"Закодированная строка: {result}")
