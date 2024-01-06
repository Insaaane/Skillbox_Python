#Задача 6. Стипендия

educational_grant = float(input("Введите стипендию: "))
expenses = float(input("Введите расходы на проживание: "))

get_from_parents = 0
missing_amount = 0

for i in range(1, 11):
    missing_amount += expenses - educational_grant
    print(f"{i} месяц траты {expenses:.1f} не хватает {missing_amount:.2f}")
    expenses *= 1.03

print(f"Нужно попросить у родителей {missing_amount:.2f} рублей")