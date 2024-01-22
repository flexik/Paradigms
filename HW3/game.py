from HW3.Tic_tac_Toe import TicTacToe

game = TicTacToe()

while True:
    game.print_board()

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    game.make_move(row, col)

    winner = game.check_winner()
    if winner:
        if winner == 'Draw':
            print("It's a draw!")
        else:
            print(f"Player {winner} wins!")
            break
