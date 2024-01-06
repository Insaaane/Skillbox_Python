#Задание 7. Считалка

people_count = int(input('Кол-во человек: '))
peoples_in_game = list(range(1, people_count + 1))
count_start = 0
counter = int(input('Какое число в считалке? '))

print(f'Значит выбывает каждый {counter}-й человек')

while len(peoples_in_game) > 1:
    print('\nТекущий круг людей:', peoples_in_game)
    print('Начало счёта с номера', peoples_in_game[count_start])

    leave = (count_start + counter - 1) % len(peoples_in_game)
    print('Выбывает человек под номером', peoples_in_game[leave])

    peoples_in_game.pop(leave)
    count_start = leave % len(peoples_in_game)

print('\nОстался человек под номером', peoples_in_game[0])
