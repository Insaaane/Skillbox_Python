#Задача 3. Файлы и папки

import os


def get_catalog_info(path):
    total_catalog_weight = 0
    catalogs_count = 0
    files_count = 0

    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            info = get_catalog_info(os.path.join(path, dir))
            total_catalog_weight += info[0]
            catalogs_count += info[1] + 1
            files_count += info[2]
        elif os.path.isfile(os.path.join(path, dir)):
            total_catalog_weight += os.path.getsize(os.path.join(path, dir))
            files_count += 1

    return total_catalog_weight, catalogs_count, files_count


catalog = get_catalog_info(input("Введите путь: "))

print(f"Размер каталога (в Кбайтах): {catalog[0] / 1024}\n"
      f"Количество подкаталогов: {catalog[1]}\n"
      f"Количество файлов: {catalog[2]}")
