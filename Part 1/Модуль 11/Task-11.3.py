#Задача 3. Аналог Steam

import math

file = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения: '))

time = math.ceil(file / speed)
downloaded = 0

for i in range(1, time + 1):
    downloaded += speed
    if downloaded > file:
        downloaded = file
    percent = round(downloaded / file * 100)
    print(f'Прошло {i} сек. Скачано {downloaded} из {file} Мб ({percent}%)')
