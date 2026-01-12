#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    # Lignes
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return True

    # Colonnes
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Diagonales
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    """Demande un coup valide (row, col) en gérant erreurs et bornes."""
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input: please enter numbers only.")
            continue

        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Invalid move: row/column must be 0, 1, or 2.")
            continue

        return row, col

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Match nul
        if board_full(board):
            print("It's a draw!")
            break

        row, col = get_move(player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        # Vérifie victoire APRÈS le coup du joueur actuel
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Change de joueur
        player = "O" if player == "X" else "X"

tic_tac_toe()
