#Задание 6. Пицца

orders = dict()
orders_count = int(input('Введите количество заказов: '))

for i in range(1, orders_count + 1):
    order = input(f'{i}-й заказ: ').split()
    customers_name = order[0]
    pizza = order[1]
    count = int(order[2])

    if customers_name not in orders:
        orders[customers_name] = {}

    orders[customers_name][pizza] = orders[customers_name].get(pizza, 0) + count

for person, pizza_count in orders.items():
    print(f'{person}:')
    for pizza, count in pizza_count.items():
        print(' ' + f'{pizza}: {count}')
