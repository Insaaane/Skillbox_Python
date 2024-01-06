#Задание 4. Марсоход-2

current_x = 8
current_y = 10

max_x = 15
max_y = 20

while True:
    movement = input("Марсоход находится на позиции " + str(current_x) + " " + str(current_y) + ", введите команду: ")
    if (movement == "w" or movement == "W") and (current_y < max_y):
        current_y+=1
    elif (movement == "s" or movement == "S") and (current_y > 0):
        current_y-=1
    elif (movement == "a" or movement == "A") and (current_x > 0):
        current_x-=1
    elif (movement == "d" or movement == "D") and (current_x < max_x):
        current_x+=1