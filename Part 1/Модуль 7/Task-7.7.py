#Задача 7. Пропавшая карточка

n = int(input("Введите количество карточек: "))
summ = 0

for i in range(1, n+1):
    summ += i
for i in range(1, n):
    card = int(input("Введите номер оставшейся карточки: "))
    summ -= card
print("Номер пропавшей карточки:", summ)
