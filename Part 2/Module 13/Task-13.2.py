#Задача 2. Пути файлов

import os.path


def gen_files_path(path='C:/'):
    result = []
    for root, dirs, files in os.walk(path):
        result += [os.path.join(root, name) for name in files]
    return result


cur_path = r'C:\Users\daybo\Desktop\pythonProject21\Part 2\Module 13'
print(gen_files_path(cur_path))
