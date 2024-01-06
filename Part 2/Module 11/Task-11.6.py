#Задача 6. Крестики-нолики

class Board:
    def __init__(self):
        self.cells = [' ' for _ in range(9)]

    def display(self):
        print('-------------')
        print('|', self.cells[0], '|', self.cells[1], '|', self.cells[2], '|')
        print('-------------')
        print('|', self.cells[3], '|', self.cells[4], '|', self.cells[5], '|')
        print('-------------')
        print('|', self.cells[6], '|', self.cells[7], '|', self.cells[8], '|')
        print('-------------')

    def update_cell(self, cell_num, player):
        if self.cells[cell_num] == ' ':
            self.cells[cell_num] = player
            return True
        else:
            return False

    def is_winner(self, player):
        win_state = [player, player, player]
        if self.cells[0:3] == win_state or self.cells[3:6] == win_state or self.cells[6:9] == win_state:
            return True
        elif self.cells[0:7:3] == win_state or self.cells[1:8:3] == win_state or self.cells[2:9:3] == win_state:
            return True
        elif self.cells[0:9:4] == win_state or self.cells[2:7:2] == win_state:
            return True
        else:
            return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_move(self):
        cell_num = input(f'{self.name}, выберите ячейку (1-9): ')
        return int(cell_num) - 1


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('Игрок 1', 'X')
        self.player2 = Player('Игрок 2', 'O')
        self.current_player = self.player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def run(self):
        print('Игра Крестики-нолики!')
        self.board.display()

        while True:
            cell_num = self.current_player.make_move()
            if self.board.update_cell(cell_num, self.current_player.symbol):
                self.board.display()
                if self.board.is_winner(self.current_player.symbol):
                    print(f'{self.current_player.name} победил!')
                    self.current_player.wins += 1
                    break
                elif ' ' not in self.board.cells:
                    print('Ничья!')
                    break
                else:
                    self.switch_player()
            else:
                print('Эта ячейка уже занята. Попробуйте снова.')

        print('Счёт:')
        print(f'{self.player1.name}: {self.player1.wins}')
        print(f'{self.player2.name}: {self.player2.wins}')

    def play_again(self):
        answer = input('Ты хочешь поиграть еще раз? (Y/N): ')
        if answer.upper() == 'Y':
            self.board = Board()
            return True
        else:
            return False

    def start(self):
        while True:
            self.run()
            if not self.play_again():
                break


game = Game()
game.start()
