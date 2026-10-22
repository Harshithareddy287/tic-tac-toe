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
    
    def has_won(self, mark):
        for row in self._grid:
            if all(cell == mark for cell in row):
                return True

        for col in range(3):
            if all(self._grid[row][col] == mark for row in range(3)):
                return True

        if all(self._grid[i][i] == mark for i in range(3)):
            return True

        if all(self._grid[i][2 - i] == mark for i in range(3)):
            return True

        return False

    def is_full(self):
        return len(self.empty_cells()) == 0
    
    # Returning board as string
    def __str__(self):
        rows = [" | ".join(row) for row in self._grid]
        return "\n---------\n".join(rows)