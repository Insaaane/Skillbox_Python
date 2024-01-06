#Задача 6. Яйца

def danger_level(x):
    return x**3 - 3 * x**2 - 12 * x + 10

def calculate_depth(danger_lvl):
    min_depth = 0
    max_depth = 4
    res = (min_depth + max_depth) / 2

    while abs(danger_level(res)) >= danger_lvl:
        if abs(danger_level(min_depth)) < abs(danger_level(max_depth)):
            max_depth = res
        else:
            min_depth = res
        res = (min_depth + max_depth) / 2
    return res

max_danger = float(input("Введите максимально допустимый уровень опасности: "))

print(f"Приблизительная глубина безопасной кладки: {calculate_depth(max_danger):.9f} м")