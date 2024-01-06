#Задача 6. Игра в кубики

cubeOne = int(input('Кубик Кости: '))
cubeTwo = int(input('Кубик владельца: '))

if cubeOne >= cubeTwo:
    print(cubeOne - cubeTwo)
    print('Игрок платит')
else:
    print(cubeOne + cubeTwo)
    print('Владелец платит')

print('Игра окончена')