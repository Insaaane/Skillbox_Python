#Задача 4. Продвинутая функция sum

def my_sum(*args):
    total = 0
    for arg in args:
        if isinstance(arg, list):
            total += my_sum(*arg)
        else:
            total += arg
    return total


print(my_sum([[1, 2, [3]], [1], 3]))
print(my_sum(1, 2, 3, 4, 5))
