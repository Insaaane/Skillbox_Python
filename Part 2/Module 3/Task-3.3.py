#Задание 3. Детали

shop = [
    ['каретка', 1200], ['шатун', 1000], ['седло', 300],
    ['педаль', 100], ['седло', 1500], ['рама', 12000],
    ['обод', 2000], ['шатун', 200], ['седло', 2700]
]

detail_name = input('Название детали: ')

count_details = 0
result_sum = 0

for detail in shop:
    if detail[0] == detail_name:
        count_details += 1
        result_sum += detail[1]

print('Количество деталей:', count_details)
print('Общая стоимость:', result_sum)
