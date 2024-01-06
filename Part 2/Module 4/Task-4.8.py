#Задание 8. Шифр Цезаря

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

message = input("Введите сообщение: ")
shift = int(input("Введите двиг: "))

encrypted_message = ""
for char in message:
    if char in alphabet:
        index = alphabet.index(char)
        shifted_index = (index + shift) % len(alphabet)
        encrypted_message += alphabet[shifted_index]
    else:
        encrypted_message += char

print("Зашифрованное сообщение:", encrypted_message)
