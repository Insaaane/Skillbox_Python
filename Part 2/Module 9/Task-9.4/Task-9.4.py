#Задача 4. Турнир

first_tour = open("first_tour.txt", "r")
second_tour = open("second_tour.txt", "w")

with first_tour, second_tour:
    min_score = int(first_tour.readline().strip())
    participants = []

    for line in first_tour:
        surname, name, score = line.strip().split()
        if int(score) > min_score:
            participants.append((surname, name[0], int(score)))

    participants.sort(key=lambda x: x[2], reverse=True)
    second_tour.write(str(len(participants)) + "\n")
    for i, participant in enumerate(participants, 1):
        second_tour.write(f"{i}) {participant[1]}. {participant[0]} {participant[2]}\n")

first_tour.close()
second_tour.close()
