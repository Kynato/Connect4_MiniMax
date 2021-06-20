from minmax import AI
from board import Board
from termcolor import colored

# CHANGE PROPERTIES HERE
MINIMAX_DEPTH = 5
GAME_WIDTH = 6
GAME_HEIGHT = 4


def report_win():
    winner = game.check_for_win()
    if winner is not None:
        if winner == 1:
            print(colored('AI has won.', 'red'))
        elif winner == -1:
            print(colored('Player has won', 'green'))
        else:
            print(colored('TIE', 'yellow'))

        print('=================')
        print('Final table state')
        game.print_table()
        return True
    return False


def welcome():
    print('CONNECT 4 - GAME')
    print(colored('O - you', 'green'))
    print(colored('X - AI', 'red'))


if __name__ == '__main__':
    print('RUNNING main.py.')

    # Initiate board
    game = Board(rows=GAME_HEIGHT, cols=GAME_WIDTH, player_turn=True)

    # Initiate AI
    AI = AI(depth=MINIMAX_DEPTH)

    welcome()

    # GAME LOOP
    while not report_win():
        # Player move
        while not game.make_move(int(input('Make a move: '))):
            print(colored('Try other move', 'yellow'))

        # AI move
        game.make_move(AI.best_move(game))

        # Render
        game.print_table()


else:
    print('IMPORTED  == main.py ==')
