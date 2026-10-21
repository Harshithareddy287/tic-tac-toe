class Board:
    def __init__(self):
        self._grid = [[" " for _ in range(3)] for _ in range(3)]

    def place_mark(self, row, col, mark):
        if not (0 <= row < 3 and 0 <= col < 3):
            return False

        if self._grid[row][col] != " ":
            return False

        self._grid[row][col] = mark
        return True

    def remove_mark(self, row, col):
        self._grid[row][col] = " "

    def empty_cells(self):
        return [
            (row, col)
            for row in range(3)
            for col in range(3)
            if self._grid[row][col] == " "
        ]