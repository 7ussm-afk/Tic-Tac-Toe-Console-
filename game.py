def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current = "X"

    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {current}, enter row (0-2): "))
        col = int(input(f"Player {current}, enter col (0-2): "))
        if board[row][col] == " ":
            board[row][col] = current
            if check_winner(board, current):
                print_board(board)
                print(f"Player {current} wins!")
                return
            current = "O" if current == "X" else "X"
        else:
            print("Cell already taken!")

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()
