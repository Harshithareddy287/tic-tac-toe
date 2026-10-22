import random
from game import Game
from ai import EasyAI, HardAI

def main():
    print("Welcome to Tic-Tac-Toe!!!")

    # Choosing game mode
    mode = input("1. Two Players\n2. Computer\nChoose mode: ")
    while mode not in ("1", "2"):
        mode = input("Invalid choice. Enter 1 or 2: ")

    ai_player = None

    # Choosing AI difficulty
    if mode == "2":
        level = input("1. Easy\n2. Hard\nChoose difficulty: ")
        while level not in ("1", "2"):
            level = input("Invalid choice. Enter 1 or 2: ")

        if level == "1":
            ai_player = EasyAI(random.Random())
        else:
            ai_player = HardAI(random.Random())

    game = Game(ai_player)
    print(game.board)

    while game.winner is None and not game.is_draw:

        # Computer plays O
        if ai_player and game.current_player == "O":
            print("\nComputer's turn")
            game.make_ai_move()
            print(game.board)
            continue

        print(f"\nPlayer {game.current_player}'s turn")
        move = input("Enter row and column (1-3): ").split()

        # Checking input
        if len(move) != 2 or not all(x.isdigit() for x in move):
            print("Invalid input.")
            continue

        # Convert to 0-based indexes
        row, col = int(move[0]) - 1, int(move[1]) - 1

        if not game.make_move(row, col):
            print("Invalid move. Try again.")
            continue

        print(game.board)

    if game.winner:
        print(f"\nPlayer {game.winner} wins!")
    else:
        print("\nIt's a draw!")


if __name__ == "__main__":
    main()
