#Задача 1. Работа с файлом 2

class File:
    def __init__(self, path: str, mode="r", encoding="UTF-8") -> None:
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.path, self.mode)
        except FileNotFoundError:
            self.file = open(self.path, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return True


with File("test.txt") as file:
    file.write("12345")

with File("test.txt") as file:
    try:
        file.write("124")
    except:
        print("Получено исключение ввода-вывода, потому что файл существует и открыт в режиме чтения")

    print("Программа работает!")