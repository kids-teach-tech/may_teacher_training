from helper import display_board, check_for_winnner, board_full, display_winning_board

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = "X"
winner = False
while winner == False:
    # Display board & get move
    display_board(board)
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    
    # Make move
    if board[row][col] == " ":
        board[row][col] = player
    else:
        print("Invalid move! Try again.")

    # Check for winner
    winner = check_for_winnner(board)
    if winner:
        print(f"{winner} wins!")
        display_winning_board(board)
    elif board_full(board):
        print("It's a draw!")

    # Switch player
    if player == "X":
        player = "O"
    else:
        player = "X"