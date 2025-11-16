import tictactoe

def main():
    game = tictactoe.TTT()
    
    # Game Loop
    while True:

        # display board
        game.display()

        # ask for player input
        move = input(f"Player {game.player}, enter your move (row and column) or 'q' to quit: ")

        # quit condition
        if move.lower() == 'q':
            print("Game exited.")
            break

        # parsing input
        try:
            row, col = map(int, move.split())
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter row and column between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input format. Please enter row and column separated by a space.")
            continue
        
        # make move (logic is hidden in tictactoe module)
        if not game.make_move(row, col):
            print("Cell already occupied. Try again.")
            continue
        
        # check for winner or draw
        winner = game.check_winner()
        if winner:
            game.display()
            print(f"Player {winner} wins!")
            game.reset()
            continue
        
        if game.is_draw():
            game.display()
            print("It's a draw!")
            game.reset()
            continue

    return 0

if __name__ == "__main__":
    main()