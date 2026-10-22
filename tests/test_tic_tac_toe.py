
from board import Board
from game import Game


# Testing X starts and players take turns
def test_players_take_turns():
    game = Game()

    assert game.current_player == "X"
    game.make_move(0, 0)
    assert game.current_player == "O"

    game.make_move(1, 1)
    assert game.current_player == "X"


# Testing invalid move does not change turn
def test_invalid_move_keeps_turn():
    game = Game()

    game.make_move(0, 0)
    assert game.make_move(0, 0) is False
    assert game.current_player == "O"


# Testing that new board has 9 empty cells
def test_new_board_has_nine_empty_cells():
    board = Board()
    assert len(board.empty_cells()) == 9


# Test that occupied cell cannot be overwritten
def test_cannot_place_mark_in_occupied_cell():
    board = Board()

    assert board.place_mark(1, 1, "X") is True
    assert board.place_mark(1, 1, "O") is False

    # Check that the original X is still in the cell
    assert board.place_mark(1, 0, "X") is True
    assert board.place_mark(1, 2, "X") is True

    assert board.has_won("X") is True
    assert board.has_won("O") is False


# Testing that moves outside board are rejected
def test_cannot_place_mark_outside_board():
    board = Board()

    assert board.place_mark(-1, 0, "X") is False
    assert board.place_mark(3, 0, "X") is False
    assert board.place_mark(0, 3, "X") is False


# Testing winning across a row
def test_row_win():
    board = Board()

    for col in range(3):
        board.place_mark(0, col, "X")

    assert board.has_won("X") is True


# Testing winning down a column
def test_column_win():
    board = Board()

    for row in range(3):
        board.place_mark(row, 1, "O")

    assert board.has_won("O") is True


# Testing winning on main diagonal
def test_main_diagonal_win():
    board = Board()

    for i in range(3):
        board.place_mark(i, i, "X")

    assert board.has_won("X") is True


# Testing win on other diagonal
def test_other_diagonal_win():
    board = Board()

    for i in range(3):
        board.place_mark(i, 2 - i, "O")

    assert board.has_won("O") is True


# Testing full board withoutwinner is draw
def test_game_draw():
    game = Game()

    moves = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (1, 2),
        (2, 1), (2, 0), (2, 2)
    ]

    for row, col in moves:
        game.make_move(row, col)

    assert game.is_draw is True
    assert game.winner is None

