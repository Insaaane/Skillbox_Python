#Задача 4. Чат

def get_action():
    print('\nВыберите одно из действий:')
    print('\t1. Посмотреть текущий текст чата.')
    print('\t2. Отправить сообщение.')
    print('\t3. Выход.')
    return input('Введите номер действия: ')


def show_chat(_chat):
    print('\nПредыдущие сообщения чата:\n')
    _chat.seek(0)
    print(_chat.read())


def new_message(username, _chat):
    message = input('Введите сообщение: ')
    _chat.write("{}: {}\n".format(username, message))


name = input('Введите ваше имя: ')
chat = open('chat.txt', 'a+', encoding='utf-8')

with chat:
    while True:
        try:
            action = get_action()
            if action == '1':
                show_chat(chat)
            elif action == '2':
                new_message(name, chat)
            elif action == '3':
                break
            else:
                print('Нет такой команды. Попробуйте ещё раз.')
        except BlockingIOError:
            print('Сейчас с чатом работает другой пользователь.')
            print('Подождите и повторите попытку позже.')
        except:
            print('Непредвиденная ошибка! Свяжитесь со службой технической поддержки.')
            break