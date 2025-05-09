def display_board(board):
    print("\nCurrent Board:")
    for row in board:
        # print(row, row[0])
        print(row[0] or " ", "|", row[1] or " ", "|", row[2] or " ")
        print("-" * 9)


def player_input(player):
    while True:
        try:
            row = int(input(f"Player {player} - Enter row (1, 2, or 3): "))
            col = int(input(f"Player {player} - Enter column (1, 2, or 3): "))
            
            if row in [1, 2, 3] and col in [1, 2, 3]:
                return row - 1, col - 1
            else:
                print("Both numbers must be 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")



def check_win(board, player):

    # print(range(3))
    for i in range(3):# Check rows
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    
    for i in range(3): # Check columns
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: # Check diagonals
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def play():
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    current_player = "X"
    moves = 0

    while moves < 9:
        display_board(board)
        row, col = player_input(current_player)

        if board[row][col] == "":
            board[row][col] = current_player
            moves += 1

            if check_win(board, current_player):
                display_board(board)
                print(f" Player {current_player} wins!")
                return
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            # print(current_player)
        else:
            print("That spot is already taken. Try another.")

    display_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        print("\n\n Goodbye a Cheriff")