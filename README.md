# Tic-Tac-Toe with AI Opponent

This is a Tic-Tac-Toe game I built using Python. The game runs in the terminal and lets two players play against each other or one player play against the computer.

I built this project to practice Python, object-oriented programming, writing tests with pytest, and using GitHub Actions.

## Features

- A 3×3 Tic-Tac-Toe board.
- Two-player mode where X and O take turns.
- Computer mode where the player is X and the computer is O.
- Two computer difficulty levels:
  - **Easy:** Chooses a random empty cell.
  - **Hard:** Uses the minimax algorithm to choose the best move and avoid losing.
- Checks for invalid moves, wins, and draws.
- Displays the board after every move.

## How to Run the Game

Make sure Python is installed on your computer.

Open the terminal in the project folder and run:

```bash
python main.py
```

When the game starts, choose one of the options:

1. Two Players
2. Computer

If you select Computer, you can choose Easy or Hard difficulty.

## How to Play

Players enter their moves using a row and column number from 1 to 3.

For example:

```text
2 3
```

This places the mark in the second row and third column.

X always goes first. If a player enters an invalid position, a cell that is already taken, or non-numeric input, the game asks them to try again without losing their turn.

The game ends when a player gets three marks in a row, column, or diagonal, or when the board is full and there is no winner.

## How to Run Tests

I used pytest to test the board, game rules, and AI players.

First, install the required packages:

```bash
pip install -r requirements.txt
```

Then run the tests:

```bash
python -m pytest
```

The project has 15 tests covering player turns, invalid moves, winning conditions, draws, and AI behavior.

## Project Structure

- `board.py` — Creates the board and checks valid moves and winning conditions.
- `game.py` — Manages player turns and game results.
- `ai.py` — Contains the Easy and Hard AI classes.
- `main.py` — Handles the menu, user input, and game display.
- `tests/` — Contains the pytest tests.
- `PLAN.md` — Explains the project requirements and design decisions.
- `.github/workflows/ci.yml` — Runs the tests automatically using GitHub Actions.

