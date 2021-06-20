

class Board:
    def __init__(self, rows:int, cols:int, player_turn:bool):
        self.rows = rows
        self.cols = cols
        self.player_turn = player_turn
        self.table = []
        self.border = 2

        self.create_table()


    def create_table(self):
        for row in range(self.rows + self.border):
            line = []
            for col in range(self.cols + self.border):
                line.append(-1)
            self.table.append(line)

        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                self.table[row][col] = 0

        print('Created table with {rows} rows and {cols} cols'.format(rows=self.rows, cols=self.cols))
    
    def print_table(self):
        i_like_coffee = ''
        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                i_like_coffee += str(self.table[row][col])
            i_like_coffee += '\n'
        print(i_like_coffee)

    def is_move_legal(self, choice:int):
        # incrementing choice so we avoid calculating borders
        choice += 1

        for row in reversed(range(1, self.rows+1)):
            if self.table[row][choice] == 0:
                return (row, choice)

        return None

    def make_move(self, choice:int):
        #print('Dropping token into {choice} row.'.format(choice=choice))

        choice += 1
        for row in reversed(range(1, self.rows+1)):
            if self.table[row][choice] == 0:
                if self.player_turn == True:
                    self.table[row][choice] = 1
                else:
                    self.table[row][choice] = 2
                break

        self.player_turn = not self.player_turn

    def get_legal_moves(self):
        moves = []
        for col in range(0, self.cols):
            coords = self.is_move_legal(col)
            if coords != None:
                moves.append(coords)

        #print('legal moves: {moves}'.format(moves=str(moves)))
        return moves

    def check_for_win(self):
        hor_score = ver_score = 0
        player = 1
        enemy = -1
        tie = 0
        not_decided = None
        # check for player horizontal win
        for row in range(1, self.rows+1):
            for col in range(1, self.cols+1):
                if self.table[row][col] == 1:
                    hor_score += 1
                else:
                    hor_score = 0
            if hor_score >= 4:
                return player
        
        # check for player vertical win
        for col in range(1, self.cols+1):
            for row in range(1, self.rows+1):
                if self.table[row][col] == 1:
                    ver_score += 1
                else:
                    ver_score = 0
            if ver_score >= 4:
                return player

        # check for ascending diagonal player win
        for row in range(1+3, self.rows+1):
            for col in range(1, self.cols+1-3):
                if self.table[row][col] == 1 and self.table[row+1][col+1] == 1 and self.table[row+2][col+2] == 1 and self.table[row+3][col+3] == 1:
                    return player
                
        # check for descending diagonal player win
        for row in range(1+3, self.rows+1):
            for col in range(1+3, self.cols+1):
                if self.table[row][col] == 1 and self.table[row-1][col-1] == 1 and self.table[row-2][col-2] == 1 and self.table[row-3][col-3] == 1:
                    return player

        hor_score = ver_score = 0
        # check for ENEMY horizontal win
        for row in range(1, self.rows+1):
            for col in range(1, self.cols+1):
                if self.table[row][col] == 2:
                    hor_score += 1
                else:
                    hor_score = 0
            if hor_score >= 4:
                return enemy
        
        # check for ENEMY vertical win
        for col in range(1, self.cols+1):
            for row in range(1, self.rows+1):
                if self.table[row][col] == 2:
                    ver_score += 1
                else:
                    ver_score = 0
            if ver_score >= 4:
                return enemy

        # check for ascending diagonal ENEMY win
        for row in range(1+3, self.rows+1):
            for col in range(1, self.cols+1-3):
                if self.table[row][col] == 2 and self.table[row+1][col+1] == 2 and self.table[row+2][col+2] == 2 and self.table[row+3][col+3] == 2:
                    return enemy
                
        # check for descending diagonal ENEMY win
        for row in range(1+3, self.rows+1):
            for col in range(1+3, self.cols+1):
                if self.table[row][col] == 2 and self.table[row-1][col-1] == 2 and self.table[row-2][col-2] == 2 and self.table[row-3][col-3] == 2:
                    return enemy
        
        # When still empty spaces on board
        for row in range(1, self.rows+1):
            for col in range(1, self.cols+1):
                if self.table[row][col] == 0:
                    return None

        # When tie
        return tie






if __name__ == '__main__':
    print('Running board.py.')

    B = Board(rows=5, cols=8, player_turn=True)

    '''# diag player win
    B.make_move(0)
    B.make_move(0)
    B.make_move(0)
    B.make_move(1)
    B.make_move(1)
    B.make_move(2)
    B.make_move(1)
    B.make_move(4)
    B.make_move(0)
    B.make_move(7)
    B.make_move(2)
    B.make_move(7)
    B.make_move(3)
    B.make_move(7)
    B.make_move(7)
    B.make_move(7)'''

    B.make_move(7)
    B.make_move(7)
    B.make_move(7)
    B.make_move(7)
    B.make_move(6)


    B.print_table()
    B.get_legal_moves()

    print('Winner is: {winner}'.format(winner = B.check_for_win()))

else:
    print('Importing board.py')