#Задание 3. Товары

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product in goods.keys():
    total_price = 0
    count = 0
    for number in store[goods[product]]:
        count += number["quantity"]
        total_price += number["quantity"] * number["price"]
    print("{0} — {1} шт., стоимость {2} руб.".format(product, count, total_price))
