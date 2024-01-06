#Задание 1. «Я стал новым пиратом!»

karamba_counter = 0

for i in range(10):
    input_text = input("Введите слово: ")
    if input_text == "Карамба" or input_text == "карамба":
        karamba_counter += 1

print("На борт принято " + str(karamba_counter) + " пиратов!")