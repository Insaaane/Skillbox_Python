#Задача 5. Маятник

def count_oscillations(start, stop):
    count = 0
    while start > stop:
        start = start - (start * 8.4 / 100)
        count += 1
    print(f"Маятник считается остановившимся через {count} колебаний")

start_A = float(input("Введите начальную амплитуду: "))
stop_A = float(input("Введите амплитуду остановки: "))

count_oscillations(start_A, stop_A)