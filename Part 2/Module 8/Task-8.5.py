#Задача 5. Список списков — 2

def flatten_list(arr):
    if not arr:
        return []

    return flatten_list(arr[:-1]) + ([arr[-1]] if not isinstance(arr[-1], list) else flatten_list(arr[-1]))


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(flatten_list(nice_list))
