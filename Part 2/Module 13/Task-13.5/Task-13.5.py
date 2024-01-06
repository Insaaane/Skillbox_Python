#Задача 5. Обработка логов

import os


def error_log_finder(path):
    with open(path, "r", encoding="UTF-8") as log_file:
        for line in log_file:
            if "ERROR" in line:
                yield line.rstrip()


file = open("errors.txt", "w")
with file:
    for i in error_log_finder(os.path.join("log.txt")):
        file.write(f"{i}\n")
