# Jonathan Alvarado
# April 18th, 2022

new_board = ["[-", "-", "-]",
             "[-", "-", "-]",
             "[-", "-", "-]"]


def board_displayed():
    print(new_board[0] + " | " + new_board[1] + " | " + new_board[2])
    print(new_board[3] + " | " + new_board[4] + " | " + new_board[5])
    print(new_board[6] + " | " + new_board[7] + " | " + new_board[8])


def start_game():
    board_displayed()


start_game()
