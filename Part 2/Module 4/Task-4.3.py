#Задание 3. Случайные соревнования

import random

team_1 = [round(random.uniform(5, 10), 2) for i in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for i in range(20)]

winners = [max(team_1[index], team_2[index]) for index in range(20)]

print(f"Первая команда: {team_1}")
print(f"Вторая команда: {team_2}")
print(f"Победители тура: {winners}")
