#Задача 4. Успеваемость в классе

n = int(input("Введите количество учеников в классе: "))
five = 0
four = 0
three = 0
print("Введите оценки всех учеников: ")
for i in range(n):
    grade = int(input())
    if grade == 5:
        five += 1
    elif grade == 4:
        four += 1
    else:
        three += 1

if five > four and five > three:
    print("Больше отличников")
elif four > five and four > three:
    print("Больше хорошистов")
else:
    print("Больше троечников")
