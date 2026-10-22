from abc import ABC, abstractmethod

# Abstract base class for AI players
class AIPlayer(ABC):
    @abstractmethod
    def choose_move(self, board, mark):
        pass


# Easy AI chooses random empty cell
class EasyAI(AIPlayer):
    def __init__(self, rng):
        self.rng = rng

    def choose_move(self, board, mark):
        return self.rng.choice(board.empty_cells())


# Hard AI using minimax to choose best move
class HardAI(AIPlayer):
    def __init__(self, rng):
        self.rng = rng

    def choose_move(self, board, mark):
        best_score = -10
        best_moves = []

        for row, col in board.empty_cells():
            board.place_mark(row, col, mark)

            # Take an immediate winning move
            if board.has_won(mark):
                board.remove_mark(row, col)
                return (row, col)

            score = self.minimax(board, mark, False)
            board.remove_mark(row, col)

            if score > best_score:
                best_score = score
                best_moves = [(row, col)]
            elif score == best_score:
                best_moves.append((row, col))

        return self.rng.choice(best_moves)

    def minimax(self, board, mark, ai_turn):
        opponent = "X" if mark == "O" else "O"

        # Score a win, loss, or draw
        if board.has_won(mark):
            return 1
        if board.has_won(opponent):
            return -1
        if board.is_full():
            return 0

        scores = []

        for row, col in board.empty_cells():
            player = mark if ai_turn else opponent

            board.place_mark(row, col, player)
            score = self.minimax(board, mark, not ai_turn)
            board.remove_mark(row, col)

            scores.append(score)

        return max(scores) if ai_turn else min(scores)
