#Задание 8. Древний палиндром

input_text = input("Введите текст палиндрома: ")
palindrome = True

for index_char in range(len(input_text)//2):
    if input_text[index_char] != input_text[-index_char-1]:
        palindrome = False
        print("Нет, это не палиндром!")
        break

if palindrome:
    print("Да, это палиндром!")