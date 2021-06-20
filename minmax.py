from board import Board


class AI:
    def __init__(self, depth: int = 0):
        # Depth of the minimax algorithm
        self.depth = depth

    # Finds the best move for the AI
    def best_move(self, board: Board):
        best_score = -9999
        move = None
        move_scores = []

        # Get all legal moves (row, col)
        legal_moves = board.get_legal_moves()

        # Surface level of minimax
        for col in legal_moves:
            board.table[col[0]][col[1]] = 2
            score = self.minimax(board, 0, False)
            move_scores.append(score)
            board.table[col[0]][col[1]] = 0
            if score > best_score:
                best_score = score
                move = col[1] - 1

        print('Legal_moves: {legals}'.format(legals=legal_moves))
        print('move_scores: {scores}'.format(scores=move_scores))
        return move

    # Minimax implementation
    def minimax(self, board: Board, depth, is_maximizing: bool):
        # Check for immediate win or tie
        result = board.check_for_win()
        if result is not None:
            return result

        # Check for depth limit
        if depth > self.depth:
            return 0  # <- maybe this should be different?

        # If maximizing
        if is_maximizing:
            best_score = -777
            legal_moves = board.get_legal_moves()
            for col in legal_moves:
                board.table[col[0]][col[1]] = 2
                score = self.minimax(board, depth + 1, False)
                board.table[col[0]][col[1]] = 0
                best_score = max(score, best_score)

            return best_score

        # else we are minimising
        else:
            best_score = 777
            legal_moves = board.get_legal_moves()
            for col in legal_moves:
                board.table[col[0]][col[1]] = 1
                score = self.minimax(board, depth + 1, True)
                board.table[col[0]][col[1]] = 0
                best_score = min(score, best_score)

            return best_score


if __name__ == '__main__':
    print('RUNNING minmax.py.')

    # Initiate board
    B = Board(rows=4, cols=4, player_turn=True)

    # AI part
    AI = AI(depth=3)

    # AI.fill_tree(B)
    AI.best_move(B)

else:
    print('IMPORTED == minmax.py ==')
