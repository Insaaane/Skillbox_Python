#Задание 6. Ролики

def get_max_people(skates, foot_size):
    result = 0
    skates_sorted_list = list(sorted(skates, reverse=True))
    for size in sorted(foot_size):
        while len(skates_sorted_list) > 0 and skates_sorted_list[-1] < size:
            skates_sorted_list.pop()
        if len(skates_sorted_list) == 0:
            break
        if skates_sorted_list[-1] == size:
            result += 1
            skates_sorted_list.pop()
    return result


count = int(input('Количество коньков: '))
skates_list = []

for people in range(1, count + 1):
    skate_size = int(input(f'Размер пары {people}: '))
    skates_list.append(skate_size)

count = int(input('Количество людей: '))
foot_size_list = []

for people in range(1, count + 1):
    foot_size = int(input(f'Размер ноги человека {people}: '))
    foot_size_list.append(foot_size)

result_peoples = get_max_people(skates_list, foot_size_list)
print('Наибольшее количество людей, которые могут взять ролики:', result_peoples)
