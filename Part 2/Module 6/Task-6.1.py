#Задание 1. Песни — 2

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

total_duration = 0
songs_count = int(input("Сколько песен выбрать? "))
current_song = 1

for i in range(songs_count):
    song_name = input(f'Название {current_song}-й песни: ')
    if song_name in violator_songs:
        total_duration += violator_songs[song_name]
        current_song += 1
    else:
        print("Такой песни нет в списке")

print("Общее время звучания песен: {:.2f} минут".format(total_duration))
