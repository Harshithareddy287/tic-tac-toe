# Tic-Tac-Toe with AI Opponent — Project Plan

## 1. Goal

The goal of this project is to build a Tic-Tac-Toe game in Python that runs in the terminal and allows two people to play against each other or one person to play against the computer. The computer will have two difficulty levels, Easy and Hard, and the game will check for valid moves, wins, and draws using object-oriented programming.

## 2. Requirements

| ID | Requirement | How to Verify |
|---|---|---|
| R1 | The game should have a 3×3 board, and X should always play first. | Test that a new board has nine empty cells and the first turn belongs to X. |
| R2 | Players should enter a row and column using numbers from 1 to 3. | Run the game and check that an input like `2 3` places the mark in the correct position. |
| R3 | Invalid inputs, occupied cells, and positions outside the board should not use up a player's turn. | Test invalid positions and occupied cells, and manually check nonnumeric input. |
| R4 | The board should be displayed after every move. | Play the game and check that the updated board appears after each move. |
| R5 | The game should recognize wins in rows, columns, and both diagonals. | Write pytest tests for each type of winning line. |
| R6 | The game should recognize a draw when the board is full and nobody has won. | Test a full board that has no winner. |
| R7 | Players should be able to choose between two-player mode and playing against the computer. | Run both modes and check that the computer plays O while the human plays X. |
| R8 | Easy AI should choose a random move from the empty cells. | Use a seeded random generator and test that the AI selects an available cell. |
| R9 | Hard AI should use minimax to make the best move and avoid losing. | Test winning and blocking moves, and check the possible game outcomes. |
| R10 | EasyAI and HardAI should inherit from an abstract AI class and implement `choose_move(board, mark)`. | Test that the abstract class cannot be created directly and that both AI classes can choose moves. |
| R11 | The board data should be kept inside the Board class, and only `main.py` should handle input and output. | Review the code to check that `_grid` is used and that `print()` and `input()` are only in `main.py`. |
| R12 | The project should have at least 12 passing pytest tests and an automated CI workflow. | Run pytest locally and check that GitHub Actions passes on pull requests and `main`. |

## 3. Components

| Component | Responsibility |
|---|---|
| `board.py` — `Board` | Store the 3×3 board and handle placing marks, removing marks, checking empty cells, wins, and full boards. |
| `ai.py` — `AIPlayer` | Define the abstract `choose_move(board, mark)` method that all AI players must implement. |
| `ai.py` — `EasyAI` | Choose a random move from the available cells using a `random.Random` object. |
| `ai.py` — `HardAI` | Use minimax to find the best possible move. |
| `game.py` | Handle player turns, valid moves, and game results without using `print()` or `input()`. |
| `main.py` | Show the game menu and board, take player input, convert row and column numbers, and display results. |
| `tests/` | Store pytest tests for the board, game rules, and AI players. |
| `conftest.py` | Store shared pytest fixtures if they are needed. |
| `requirements.txt` | List the Python packages needed for the project tests. |
| `.github/workflows/ci.yml` | Run pytest automatically when a pull request is opened or changes are pushed to `main`. |
| `README.md` | Explain how to install, run, and play the game, and how to run the tests. |
| `PLAN.md` | Keep the project plan, requirements, design decisions, and final changes. |

## 4. Decisions

### Decision 1: How to store the board

**Options considered:**
- Use one list with nine cells.
- Use a nested list with three rows and three columns.

**My choice:** Use a nested list.

**Why:** I chose a nested list because it makes it easier to work with rows and columns. It also matches what I learned in the Lists and Nested Lists article. The board will be stored in `_grid`, and other parts of the program will use the Board methods instead of accessing the grid directly.

The Board class will include these required methods:

- `place_mark(row, col, mark)`
- `remove_mark(row, col)`
- `empty_cells()`
- `has_won(mark)`
- `is_full()`

### Decision 2: How to organize the AI players

**Options considered:**
- Put both Easy and Hard AI logic in one function using conditions.
- Create an abstract AI class with separate EasyAI and HardAI classes.

**My choice:** Use an abstract AI class with two subclasses.

**Why:** This approach helps me apply inheritance, abstraction, and polymorphism from the OOP articles. Both AI classes will have a `choose_move(board, mark)` method, so the game can call the same method for either difficulty level.

### Decision 3: How Hard AI will choose moves

**Options considered:**
- Pick a random empty cell.
- Use minimax to check possible future moves.

**My choice:** Use the minimax algorithm.

**Why:** Random moves are enough for Easy mode, but Hard mode needs to make better decisions. Minimax will help the computer check possible outcomes and choose moves that prevent it from losing.

The Hard AI will use the Board methods to try moves and undo them while searching, without changing the board permanently.

### Decision 4: How to develop and test the project

**Options considered:**
- Finish writing the game and test everything afterward.
- Build the game in smaller parts and test each part as I go.

**My choice:** Build and test the project step by step.

**Why:** I think this will make it easier to find mistakes and understand how each part works. I will use pytest to test the game logic and GitHub Actions to check the tests automatically.

I will work on two feature branches:

1. `feature/board-and-rules` — Create the Board class, implement the two-player game, write board tests, and add CI.
2. `feature/ai-opponents` — Add Easy and Hard AI, computer mode, more tests, and finish the documentation.

## 5. What changed

I followed most of my original plan without making any major changes to the design. I created separate classes for the Board, game logic, and AI players as planned.

I used a nested list to store the board and kept it private using `_grid`. I also used an abstract AI class with EasyAI and HardAI subclasses. EasyAI picks random available moves, while HardAI uses minimax to find the best move.

I added 15 pytest tests to check the board, player turns, invalid moves, wins, draws, and AI behavior. I also included a test to check that HardAI does not lose when playing second.

I completed the project using two feature branches, `feature/board-and-rules` and `feature/ai-opponents`, and used GitHub Actions to run the tests automatically.
