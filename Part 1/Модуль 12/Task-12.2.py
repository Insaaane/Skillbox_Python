def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


def test():
    num = int(input("Введите целое число: "))
    if num > 0:
        positive()
    elif num < 0:
        negative()


test()
