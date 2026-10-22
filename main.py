from game import Game


def main():
    game = Game()

    print("Welcome to Tic-Tac-Toe!!!")
    print("Two-player mode")
    print(game.board)

    while game.winner is None and not game.is_draw:
        print(f"\nPlayer {game.current_player}'s turn")

        move = input("Enter row and column (1-3): ").split()

        # Checking for two valid numbers
        if len(move) != 2 or not all(value.isdigit() for value in move):
            print("Invalid input. Enter two numbers.")
            continue

        # Converting to 0-based indexes
        row = int(move[0]) - 1
        col = int(move[1]) - 1

        # Rejecting invalid or occupied moves
        if not game.make_move(row, col):
            print("Invalid move. Try again.")
            continue

        # Displaying board after valid move
        print(game.board)

    if game.winner:
        print(f"\nPlayer {game.winner} wins!")
    else:
        print("\nIt's a draw!")


if __name__ == "__main__":
    main()
