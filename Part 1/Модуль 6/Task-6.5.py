#Задача 5. Обычный день на работе

print("Начался восьмичасовой рабочий день.")
numbers_of_tasks = 0;
need_to_go_store = False;
hour = 0

while hour < 8:
    hour+=1
    print(str(hour) + " час")
    numbers_of_tasks += int(input("Сколько задач решит Максим? "))
    current_call = bool(int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): ")))
    if current_call:
        need_to_go_store = True

print("Рабочий день закончился. Всего выполнено задач: " + str(numbers_of_tasks))

if need_to_go_store:
    print("Нужно зайти в магазин.")
