#Задача 1. Квадраты чисел

class SquaresIterator:
    def __init__(self, num):
        self.n = num
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration


n = int(input("Введите число N: "))

print('Класс-итератор:')
squares_iter = SquaresIterator(n)
for square in squares_iter:
    print(square, end=' ')
print()


def generate_squares(num):
    for i in range(1, num + 1):
        yield i ** 2


print('Функция-генератор:')
for square in generate_squares(n):
    print(square, end=' ')
print()


print('Генераторное выражение:')
squares = (i ** 2 for i in range(1, n+1))
for square in squares:
    print(square, end=' ')
