#Задача 3. Палиндром: возвращение

from collections import Counter


def can_be_palindrome(string: str) -> bool:
    return 1 >= sum(1 for i in Counter(string).values() if i % 2 == 1)


print(can_be_palindrome('abcba'))
print(can_be_palindrome('abbbc'))
