#Задача 6. Быстрая сортировка

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    sep = arr[-1]
    left = []
    mid = []
    right = []
    for a in arr:
        if a < sep:
            left.append(a)
        elif a == sep:
            mid.append(a)
        else:
            right.append(a)
    return quick_sort(left) + mid + quick_sort(right)


x = [1, 2, 3, 5, 2, 3, -7, 3, 0, 0, 11, 6]

print(quick_sort(x))
