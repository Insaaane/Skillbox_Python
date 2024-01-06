import random


def rock_paper_scissors():
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    computer_choice = random.choice(["камень", "ножницы", "бумага"])

    print(f"Компьютер выбрал {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (
        (user_choice == "камень" and computer_choice == "ножницы") or
        (user_choice == "ножницы" and computer_choice == "бумага") or
        (user_choice == "бумага" and computer_choice == "камень")
    ):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")


def guess_the_number():
    secret_number = random.randint(1, 10)

    while True:
        user_guess = int(input("Угадайте число от 1 до 10: "))

        if user_guess == secret_number:
            print(f"Поздравляю! Вы угадали число!")
            break


def mainMenu():
    choice = input('Выбери игру: «Камень, ножницы, бумага» (1) или «Угадай число» (2) ')
    if choice == '1':
        rock_paper_scissors()
    else:
        guess_the_number()


mainMenu()
