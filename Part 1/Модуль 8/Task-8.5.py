#Задача 5. Функция

start = int(input("Введите начало отрезка: "))
stop = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))

if step > 0:
    step = -step

if start < stop:
    start, stop = stop, start

for x in range(start, stop-1, step):
    func = x**3 + 2*x**2 - 4*x + 1
    print("В точке", x, "функция равна", func)
