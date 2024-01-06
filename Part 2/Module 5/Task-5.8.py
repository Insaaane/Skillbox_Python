#Задание 8. Бегущая строка

def get_shift_string(string, offset):
    return "".join(["".join(string[offset:]), "".join(string[:offset])])


string_1 = input("Первая строка: ")
string_2 = input("Вторая строка: ")

for shift in range(len(string_1)):
    if get_shift_string(string_1, shift) == string_2:
        print(f"Первая строка получается из второй со сдвигом {shift}")
        break
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига")
