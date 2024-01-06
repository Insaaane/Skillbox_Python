#Задание 5. Разворот

string = input('Введите строку: ')

first_h = string.index('h')
last_h = len(string) - 1 - string[::-1].index('h')
revers_between_h = string[last_h - 1:first_h:-1]

print('Развёрнутая последовательность между первым и последним h:', revers_between_h)
