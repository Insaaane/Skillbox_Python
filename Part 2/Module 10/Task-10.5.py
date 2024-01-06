#Задача 5. Надёжные вычисления

def get_square_root(num):
    try:
        if num < 0:
            raise ValueError("Не удается вычислить квадратный корень из отрицательного числа!")
        else:
            return num**0.5
    except ValueError as exc:
        print(exc)
    except TypeError:
        print("Введенное значение должно быть числом!")


print(get_square_root(16))
print(get_square_root('four'))
print(get_square_root(-4))
