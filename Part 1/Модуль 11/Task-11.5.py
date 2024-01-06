#Задача 5. Вот это объёмы!
import math

r_planet = float(input('Введите радиус случайной планет: '))

v_earth = 1.08321 * 10 ** 12
v_planet = 4/3 * math.pi * r_planet**3

if v_earth > v_planet:
    difference = v_earth / v_planet
    print(f'Объём планеты Земля больше в {difference:.3f} раз')
else:
    difference = v_planet / v_earth
    print(f'Объём планеты Земля меньше в {difference:.3f} раз')

