#Задача 5. Песни

violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56], ['Halo', 4.9],
                  ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76],
                  ['Blue Dress', 4.29], ['Clean', 5.83]]

songs_count = int(input("Сколько песен выбрать? "))
total_duration = 0

for num in range(1, songs_count+1):
    name = input(f"Название {num} песни: ")
    for song in violator_songs:
        if song[0] == name:
            total_duration += song[1]

print(f"Общее время звучания песен — {total_duration} минуты")
