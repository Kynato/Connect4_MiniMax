from anytree import AnyNode, RenderTree
from anytree.exporter import DotExporter
from board import Board
import copy
import random



class AI:
    def __init__(self, depth:int = 0):
        self.depth = depth

    def best_move(self, board:Board):
        best_score = -9999
        move = None
        # Get all legal moves (row, col)
        legal_moves = board.get_legal_moves()
        print('Legal_moves:')
        print(legal_moves)

        for col in legal_moves:
            board.table[col[0]][col[1]] == 2
            score = self.minimax(board, 0, False)
            print(score)
            board.table[col[0]][col[1]] == 0
            if score > best_score:
                best_score = score
                move = col[1]-1

        return move

    def minimax(self, board:Board, depth, isMaximizing:bool):
        # Check for immadiate win or tie
        result = board.check_for_win()
        if result != None:
            return result

        # Check for depth limit
        if depth > self.depth:
            return 0 # <- maybe this should be different?

        
        

        # If maximizing
        if isMaximizing:
            best_score = -777
            legal_moves = board.get_legal_moves()
            for col in legal_moves:
                board.table[col[0]][col[1]] = 2
                score = self.minimax(board, depth+1, False)
                board.table[col[0]][col[1]] = 0
                best_score = max(score, best_score)

            return best_score

        # else we are minimising
        else:
            best_score = 777
            legal_moves = board.get_legal_moves()
            for col in legal_moves:
                board.table[col[0]][col[1]] = 1
                score = self.minimax(board, depth+1, True)
                board.table[col[0]][col[1]] = 0
                best_score = min(score, best_score)

            return best_score



    '''def fill_tree(self, B:Board):
        index = 0
        self.root = AnyNode(board = copy.deepcopy(B), depth = 0, id = index, score=B.check_for_win(), minmax=0)
        index += 1
        
        for dep in range(self.depth):
            print('DEPTH: {depth}'.format(depth = dep))
            #print(self.root.leaves)

            for child in self.root.leaves:
                backup = copy.deepcopy(child.board)
                available_moves = child.board.get_legal_moves()

                for move in available_moves:
                    child.board.make_move(move)
                    AnyNode(parent=child, val=move, board = copy.deepcopy(child.board), depth=dep, id=index, score=child.board.check_for_win(), minmax=0)
                    index += 1
                    child.board = copy.deepcopy(backup)
                    

        # print the tree
        #print(RenderTree(self.root))
        B.print_table()

    def minmax(self, player_or_enemy:bool, depth):

        leaves = self.root.leaves
        winners = []
        not_losers = []

        for leave in leaves:
            if leave.score == player_or_enemy:
                winners.append(leave)

        if len(winners) == 0:
            lose = 0
            if player_or_enemy == 0:
                lose = 1

            for leave in leaves:
                if leave.score != lose:
                    not_losers.append(leave)

            absolute_not_loser = not_losers[0]
            for nl in not_losers:
                if absolute_not_loser.depth > nl.depth:
                    absolute_not_loser = nl

            print('Playing not to lose')
            self.print_winner(absolute_not_loser)
            return absolute_not_loser

        absolute_winner = winners[0]
        for win in winners:
            if absolute_winner.depth > win.depth:
                absolute_winner = win

        print('Found winning strategy')
        print(absolute_winner)
        self.print_winner(absolute_winner)
        return absolute_winner

    def pick_move(self, player_or_enemy:int):

        win = self.minmax(player_or_enemy)

        if win == None or win == self.root:
            legal_moves = self.root.board.get_legal_moves()
            return random.choice(legal_moves)

        while win.parent != self.root:
            win = win.parent
        return win.val'''

    '''def print_winner(self, strategy:AnyNode):
        while strategy.parent != None:
            print(strategy.val)
            strategy = strategy.parent'''






if __name__ == '__main__':
    print('Running minmax.py.')

    # Initiate board
    B = Board(rows=4, cols=4, player_turn=True)


    # AI part
    AI = AI(depth=3)

    #AI.fill_tree(B)
    AI.best_move(B)


else:
    print('Importing minmax.py')