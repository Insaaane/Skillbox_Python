#Задание 5. Контейнеры

def get_new_pos(containers, new_weight):
    for i in range(len(containers)):
        if new_weight > containers[i]:
            return i + 1
    return len(containers)


containers_list = []
count = int(input('Количество контейнеров: '))

for i in range(count):
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('Ошибка! Вес не должен превышать 200.')
        quit()
    containers_list.append(weight)

new_container = int(input('Введите вес нового контейнера: '))

print('Номер, который получит новый контейнер:', get_new_pos(containers_list, new_container))
