#Задача 7. Почта

current_time = int(input("Напишите час, когда хотите прийти: "))

if ((8 <= current_time < 22) and
    not ((14 == current_time) or (10 <= current_time < 12) or (18 <= current_time < 20))):
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")