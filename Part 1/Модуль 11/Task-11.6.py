#Задача 6. Ход конём

print('Введите местоположение коня')
x_knight = float(input())
y_knight = float(input())
print('Введите местоположение точки на доске')
x_point = float(input())
y_point = float(input())

x_knight = int(x_knight * 10)
y_knight = int(y_knight * 10)

x_point = int(x_point * 10)
y_point = int(y_point * 10)

print(f'Конь в клетке ({x_knight}, {y_knight}). Точка в клетке ({x_point}, {y_point}).')

dx = abs(x_knight - x_point)
dy = abs(y_knight - y_point)

can_move = (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

if can_move:
    print(f"Конь может ходить в эту точку.")
else:
    print(f"Конь не может ходить в эту точку.")