#Задача 3. Регистрация

def check_correct(line):
    tokens = line.split()
    if len(tokens) != 3:
        raise IndexError('Данные неполные. Отсутствуют нужное кол-во полей')
    if not tokens[0].isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    if not ('@' in tokens[1] and '.' in tokens[1]):
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
    if not (tokens[2].isnumeric() and (10 <= int(tokens[2]) <= 99)):
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')


registrations = open('registrations.txt', 'r', encoding='utf-8')
good_log = open('registrations_good.log', 'w', encoding='utf-8')
bad_log = open('registrations_bad.log', 'w', encoding='utf-8')

with registrations, good_log, bad_log:
    for line in registrations:
        line = line.replace('\n', '')
        try:
            check_correct(line)
        except Exception as e:
            bad_log.write(f'{line}\t{str(e)}\n')
        else:
            good_log.write(f'{line}\n')
