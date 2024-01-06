#Задача 1. Имена 2

people = open('people.txt', 'r', encoding='utf-8')
log = open('errors.log', 'a', encoding='utf-8')

error_text = 'Ошибка: менее трёх символов в строке {}.'
symbols_count = 0

with people, log:
    for line_i, line in enumerate(people):
        try:
            length = len(line) - line.count('\n')
            symbols_count += length
            if length < 3:
                raise ValueError(error_text.format(line_i + 1))
        except ValueError:
            print(error_text.format(line_i + 1))
            log.write(error_text.format(line_i + 1) + '\n')

print(f'Общее количество символов: {symbols_count}.')
