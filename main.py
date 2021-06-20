from minmax import AI
from board import Board

if __name__ == '__main__':
    print('Running main.py.')

    # Initiate board
    game = Board(rows=4, cols=4, player_turn=True)
    


    # AI part
    AI = AI(depth=6)

    while(True):
        
        
        player_choice = input('Make a move:')
        game.make_move(int(player_choice))
        
        winner = game.check_for_win()
        if winner != 0 and winner != None:
            if winner == 1:
                print('Player has won.')
            else:
                print('AI has won.')
            game.print_table()
            break

        game.make_move(AI.best_move(game))
        game.print_table()

        winner = game.check_for_win()
        if winner != 0 and winner != None:
            if winner == 1:
                print('Player has won.')
            else:
                print('AI has won.')
            break



else:
    print('Importing main.py')