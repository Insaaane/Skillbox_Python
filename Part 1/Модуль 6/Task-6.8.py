#Задача 8. Игра «Компьютер угадывает число»

left_position = 1
right_position = 100
estimated_number = (left_position+right_position)//2

while True:
    print("Твоё число равно, меньше или больше, чем число ", estimated_number, "?")
    answer = int(input("1 - равно, 2 - больше, 3 - меньше: "))

    if answer == 1:
        print("Я угадал число! Это же ", estimated_number)
        break
    elif answer == 2:
        left_position = estimated_number
    else:
        right_position = estimated_number

    estimated_number = (left_position + right_position) // 2