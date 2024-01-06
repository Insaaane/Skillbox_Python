#Задание 4. Вечеринка

guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
change = ""

while change != "Пора спать":
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    change = input("Гость пришёл или ушёл? ")

    if change == "ушёл":
        guest_name = input("Имя гостя: ")
        guests.remove(guest_name)
        print(f"Пока, {guest_name}!")
    elif change == "пришёл":
        guest_name = input("Имя гостя: ")
        if len(guests) <= 5:
            guests.append(guest_name)
        else:
            print("Прости, Гоша, но мест нет.")

print("Вечеринка закончилась, все легли спать.")
