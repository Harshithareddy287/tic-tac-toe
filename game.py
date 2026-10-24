from board import Board

class Game:
    def __init__(self, ai_player=None):
        self.board = Board()
        self.current_player = "X"
        self.winner = None
        self.is_draw = False
        self.ai_player = ai_player

    def make_move(self, row, col):
        # Stop moves after game has ended
        if self.winner is not None or self.is_draw:
            return False

        # Rejecting invalid moves without changing turns
        if not self.board.place_mark(row, col, self.current_player):
            return False

        # Checking whether player has won
        if self.board.has_won(self.current_player):
            self.winner = self.current_player

        # Checking for a draw
        elif self.board.is_full():
            self.is_draw = True

        # Switch turns if game is still running
        else:
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

        return True

    # Computer makes a move as O
    def make_ai_move(self):
        if self.ai_player is None or self.current_player != "O":
            return False

        if self.winner is not None or self.is_draw:
            return False

        row, col = self.ai_player.choose_move(self.board, "O")
        return self.make_move(row, col)