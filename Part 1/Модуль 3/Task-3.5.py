#Задача 5. Часы

time = int(input('Время в минутах: '))
hours = time // 60
minutes = time % 60

print('Часы: ' + str(hours))
print('Минуты: ' + str(minutes))
