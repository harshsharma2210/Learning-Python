# Getting clear output from Ipython
from IPython.display import clear_output
# randomly making a player start first
import random


class Game:
    # Creating the tic tac board
    def display_board(self, board):
        clear_output()  # For clearing output everytime
        # Making board using print statement and board as list
        self.board=board;
        print('   |   |')
        print(' ' + self.board[7] + ' | ' +
              self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' +
              self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' +
              self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    # For taking input from the user
    def player_input(self):
        # setting marker as null
        marker = ""
        # checking if marker is X or O
        while not (marker == 'X' or marker == 'O'):
            marker = input('Player 1: Do you want to be X or O? ').upper()
            # returning marker tuple
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    # for placing the marker on board
    def place_marker(self, board, marker, position):
        self.board=board;
        self.marker=marker;
        self.position=position;
        self.board[self.position] = self.marker

    # defining all the win conditions
    def win_check(self, board, mark):
        self.board=board;
        self.mark=mark;
        return ((self.board[7] == self.mark and self.board[8] == self.mark and self.board[9] == self.mark) or  # across the top
                # across the middle
                (self.board[4] == self.mark and self.board[5] == self.mark and self.board[6] == self.mark) or
                # across the bottom
                (self.board[1] == self.mark and self.board[2] == self.mark and self.board[3] == self.mark) or
                # down the middle
                (self.board[7] == self.mark and self.board[4] == self.mark and self.board[1] == self.mark) or
                # down the middle
                (self.board[8] == self.mark and self.board[5] == self.mark and self.board[2] == self.mark) or
                # down the right side
                (self.board[9] == self.mark and self.board[6] == self.mark and self.board[3] == self.mark) or
                # diagonal
                (self.board[7] == self.mark and self.board[5] == self.mark and self.board[3] == self.mark) or
                (self.board[9] == self.mark and self.board[5] == self.mark and self.board[1] == self.mark))  # diagonal

    def choose_first(self):
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'

    # to check if the space is available at that position
    def space_check(self, board, position):
        self.board=board;
        self.position=position;
        return self.board[self.position] == ' '

    # to check if board is full
    def full_board_check(self, board):
        self.board=board;
        for i in range(1, 10):
            if self.space_check(self.board, i):
                return False
        return True

    # to get choice of postion from user
    def player_choice(self, board):
        position = 0
        self.board=board;
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.space_check(self.board, position):
            position = int(input('Choose your next position: (1-9) '))

        return position

    # to play agaim
    def replay(self):
        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')
new_game = Game()

while True:
    # To Reset the board
    theBoard = [' '] * 10
    # To get marker
    player1_marker, player2_marker = new_game.player_input()
    # To get turn
    turn = new_game.choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            new_game.display_board(theBoard)
            position = new_game.player_choice(theBoard)
            new_game.place_marker(theBoard, player1_marker, position)

            if new_game.win_check(theBoard, player1_marker):
                new_game.display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if new_game.full_board_check(theBoard):
                    new_game.display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            new_game.display_board(theBoard)
            position = new_game.player_choice(theBoard)
            new_game.place_marker(theBoard, player2_marker, position)

            if new_game.win_check(theBoard, player2_marker):
                new_game.display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if new_game.full_board_check(theBoard):
                    new_game.display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not new_game.replay():
        break
