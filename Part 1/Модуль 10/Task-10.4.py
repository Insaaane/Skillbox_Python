#Задание 4. Простые числа

def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

numbers = int(input("Введите количество чисел: "))
prime_counter = 0
for _ in range(numbers):
    if is_prime(int(input("Введите число: "))):
        prime_counter += 1

print("Количество простых чисел в последовательности:", prime_counter)