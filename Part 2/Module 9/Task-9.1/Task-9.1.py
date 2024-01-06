#Задача 1. Сумма чисел 2

numbers = open('numbers.txt', 'r')
answer = open('answer.txt', 'w')
summ = 0

print("Содержимое файла numbers.txt:")

for line in numbers:
    print(line, end='')
    summ += int(line.strip())

with answer as numbers:
    numbers.write(str(summ))
    print("\nСодержимое файла answer.txt:")
    print(summ)

numbers.close()
answer.close()
