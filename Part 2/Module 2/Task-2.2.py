#Задание 2. Турнир

def get_even_elements(participants):
    return [participants[i] for i in list(range(0, len(participants), 2))]


participants = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

print('Первый день:', get_even_elements(participants))