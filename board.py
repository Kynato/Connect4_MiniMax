class Board:
    def __init__(self, rows:int, cols:int, player_turn:bool):
        self.rows = rows
        self.cols = cols
        self.player_turn = player_turn
        self.table = []
        self.border = 2

        self.create_table()
        self.print_table()


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
                return True

        return False

    def make_move(self, choice:int):
        print('Dropping token into {choice} row.'.format(choice=choice))

        choice += 1
        for row in reversed(range(1, self.rows+1)):
            if self.table[row][choice] == 0:
                if self.player_turn == True:
                    self.table[row][choice] = 1
                else:
                    self.table[row][choice] = 2
                break

        self.player_turn = not self.player_turn






if __name__ == '__main__':
    print('Running board.py.')

    B = Board(rows=5, cols=8, player_turn=True)
    print(B.is_move_legal(0))
    print(B.make_move(0))
    print(B.make_move(0))
    print(B.make_move(0))
    print(B.make_move(0))
    B.print_table()


else:
    print('Importing board.py')