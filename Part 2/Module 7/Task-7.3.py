#Задача 3. Игроки

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

result = []

for key, value in players.items():
    result.append(key + value)

print(result)
