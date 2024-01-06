#Задача 5. Частотный анализ

text = open("text.txt", "r").read()

text = ''.join(filter(str.isalpha, text)).lower()
letters_count = {}

for letter in text:
    if letter in letters_count:
        letters_count[letter] += 1
    else:
        letters_count[letter] = 1

total_letters = sum(letters_count.values())
letters_freq = [(letter, count/total_letters) for letter, count in letters_count.items()]
letters_freq.sort(key=lambda x: (-x[1], x[0]))

with open("analysis.txt", "w") as analysis:
    for letter, frequency in letters_freq:
        analysis.write(f"{letter} {frequency:.3f}\n")
