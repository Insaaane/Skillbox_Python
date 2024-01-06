#Задача 1. Драка

import random


class Unit:
    def __init__(self, name, heath=100, damage=20):
        self.name = name
        self.health = heath
        self.damage = damage

    def get_damage(self, damage):
        self.health = max(0, self.health - damage)

    def is_dead(self):
        return self.health == 0


unit_1 = Unit('Конор')
unit_2 = Unit('Хабиб')

while True:
    turn = random.randint(1, 2)

    if turn == 1:
        attacker = unit_1
        defender = unit_2
    else:
        attacker = unit_2
        defender = unit_1

    defender.get_damage(attacker.damage)

    print('{} нанес {} урона {}'.format(attacker.name, attacker.damage, defender.name))
    print('Здоровье {}: {}'.format(attacker.name, attacker.health))
    print('Здоровье {}: {}'.format(defender.name, defender.health))
    print()

    if defender.is_dead():
        print(f'{defender.name} погиб.')
        print(f'{attacker.name} одержал победу!')
        break

    (attacker, defender) = (defender, attacker)
