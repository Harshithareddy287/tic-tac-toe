from board import Board


def test_new_board_has_nine_empty_cells():
    board = Board()
    assert len(board.empty_cells()) == 9


def test_place_mark_in_empty_cell():
    board = Board()

    assert board.place_mark(0, 0, "X") is True
    assert (0, 0) not in board.empty_cells()


def test_cannot_place_mark_in_occupied_cell():
    board = Board()

    board.place_mark(1, 1, "X")
    assert board.place_mark(1, 1, "O") is False


def test_cannot_place_mark_outside_board():
    board = Board()

    assert board.place_mark(-1, 0, "X") is False
    assert board.place_mark(3, 0, "X") is False
    assert board.place_mark(0, 3, "X") is False


def test_remove_mark():
    board = Board()

    board.place_mark(2, 2, "O")
    board.remove_mark(2, 2)

    assert (2, 2) in board.empty_cells()

def test_occupied_cell_can_be_removed():
    board = Board()

    assert board.place_mark(1, 1, "X") is True
    assert board.place_mark(1, 1, "O") is False

    board.remove_mark(1, 1)
    assert (1, 1) in board.empty_cells()