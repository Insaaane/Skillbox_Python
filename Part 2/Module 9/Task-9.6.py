#Задача 6. «Война и мир»

#Архива в задании не дано

def get_letters_count(file_path):
    file = open(file_path, 'r', encoding='utf-8')
    result = dict()

    while True:
        symbol = file.read(1)
        if len(symbol) == 0:
            break
        if not symbol.isalpha():
            continue
        result[symbol] = result.get(symbol, 0) + 1

    return sorted(result.items(), key=lambda x: x[1], reverse=True)
