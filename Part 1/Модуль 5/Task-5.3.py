#Задача 3. Поступление

position = int(input("Введите место в списке поступающих: "))

if position > 10:
    print("К сожалению, вы не поступили.")
else:
    total_points = int(input("Введите количество баллов за экзамены:"))
    print("Поздравляем, вы поступили!")
    if total_points >= 290:
        print("Бонусом вам будет начисляться стипендия.")
    else:
        print("Но вам не хватило баллов для стипендии.")