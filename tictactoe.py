# imports here:


# aliases for players
X = "X"
O = "O"


class TTT:
    def __init__(self) -> None:
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = X  # default X first

    def display(self) -> None:
        for row in self.board:
            print("|".join(row))
            print("-" * 5)
    
    def str_display(self) -> str:
        display_str = ""
        for row in self.board:
            display_str += "|".join(row) + "\n"
            display_str += "-" * 5 + "\n"
        return display_str
    
    def make_move(self, row: int, col: int) -> bool:
        if self.board[row][col] == ' ':
            self.board[row][col] = self.player
            self.player = O if self.player == X else X
            return True
        return False
    
    def check_winner(self) -> str | None:
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_draw(self) -> bool:
        for row in self.board:
            if ' ' in row:
                return False
        return self.check_winner() is None
    
    def reset(self) -> None:
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = X


# for testing
def main():
    game = TTT()
    game.display()
    return 0


if __name__ == "__main__":
    main()