#Задача 5. Функция сортировки

def tpl_sort(obj):
    for elem in obj:
        if not isinstance(elem, int):
            return None
    return tuple(sorted(obj))


tpl = (6, 3, -1, 8, 4, 10, -5)

print(tpl_sort(tpl))
