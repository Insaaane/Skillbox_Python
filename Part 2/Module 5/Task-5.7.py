#Задание 7. IP-адрес 2

def check_ip(ip):
    ip_sections = ip.split('.')
    if len(ip_sections) != 4:
        return 'Адрес — это четыре числа, разделённые точками.'

    not_int_sections = [part for part in ip_sections if not part.isnumeric()]
    if len(not_int_sections) > 0:
        return ''.join([f'{part} — это не целое число.' for part in not_int_sections])

    wrong_int_sections = [section for section in ip_sections if int(section) > 255]
    if len(wrong_int_sections) > 0:
        return ''.join([f'{section} превышает 255.' for section in wrong_int_sections])

    return 'IP-адрес корректен.'


ip_address = input('Введите IP: ')
print(check_ip(ip_address))
