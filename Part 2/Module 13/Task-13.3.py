#Задача 3. Количество строк

import os.path


def get_python_files_lines_count(path='C:/'):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="UTF-8") as python_file:
                    yield len([0 for i in python_file.readlines()
                               if i.rstrip() != "" and not i.rstrip().startswith("#")])


cur_path = r'C:\Users\daybo\Desktop\pythonProject21\Part 2\Module 13'
print([i for i in get_python_files_lines_count(cur_path)])
