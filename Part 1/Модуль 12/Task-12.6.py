import math

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print('Наибольший общий делитель: ', a + b)

gcd(30, 20)