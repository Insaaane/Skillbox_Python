#Задание 7. Анализ слова — 2

def is_palindrome(s):
    return s == s[::-1]


word = input('Введите слово: ')

if is_palindrome(word):
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
