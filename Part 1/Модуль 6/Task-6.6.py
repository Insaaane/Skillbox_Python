#Задача 6. Вклады

deposit = int(input("Начальная сумма депозита: "))
percent = int(input("Годовой процент: "))
purpose = int(input("Итоговая сумма: "))

count_year = 0

while deposit < purpose:
    count_year += 1
    deposit *= (percent / 100 + 1)
    deposit = int(deposit)

print("Депозит достигнет своей цели через " + str(count_year) + " лет.")