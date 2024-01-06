#Задача 8. Кинотеатр

boys = int(input("Введите количество мальчиков: "))
girls = int(input("Введите количество девочек: "))

answer = ''

if (boys > 2 * girls) or (girls > 2 * boys):
    print("Нет решения")
elif boys >= girls:
    k = boys - girls
    for i in range(k):
        answer += "BGB"
    for i in range(girls - k):
        answer += "BG"
else:
    k = girls - boys
    for i in range(k):
        answer += "GBG"
    for i in range(boys - k):
        answer += "GB"

print(answer)
