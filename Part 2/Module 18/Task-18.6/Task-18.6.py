#Задача 6. Поиск разницы между двумя JSON-файлами

import json


def get_difference(old: dict, new: dict, diffs: dict):
    for key in old.keys():
        if key in old and key in new:
            if type(old[key]) is dict and type(new[key]) is dict:
                get_difference(old[key], new[key], diffs)
            else:
                if key in diff_list and old[key] != new[key]:
                    diffs[key] = new[key]


with open('json_old.json', 'r', encoding="UTF-8") as file:
    data_old = json.load(file)

with open('json_new.json', 'r', encoding="UTF-8") as file:
    data_new = json.load(file)

result = {}
diff_list = ['services', 'staff', 'datetime']
get_difference(data_old, data_new, result)
print(result)

with open("result.json", "w", encoding="UTF-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
