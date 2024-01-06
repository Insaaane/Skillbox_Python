#Задание 7. Пирамидка-2

n = int(input('Сколько уровней в таблице?'))
k = 1

for i in range(1, n + 1):
  print("\t" * (n - i), end="")
  for j in range(i):
    print(k, end="")
    print("\t" * 2, end="")
    k += 2
  print()