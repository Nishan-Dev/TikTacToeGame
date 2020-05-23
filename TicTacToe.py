# global variables
# if game is still going
game_still_going = True
winner = None
# whos turn is it
current_player = "x"


board = ["_", "_", "_",
        "_", "_", "_",
        "_", "_", "_"]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
# play a game of tic tac toe
def play_game():
    display_board() # display the game board
# while the game is still going
    while game_still_going:
        handle_turn(current_player)
    # check if the game is over
        check_if_game_over()
    # flip to the other player
        flip_player()
if winner =="x" or winner == "o":
    print(winner + "won.")
elif winner == None:
    print("Tie.")

def handle_turn(player):
    print(player + "'s turn")
    position = input("enter a position 0-8: ")

    valid = False
    while not valid:

     while position not in ["1","2","3","4","5","6","7","8","0"]:
        position = input("invalid input. choose a position from 0-8: ")

     if board[position] == "-":
         valid = True
    else:
        print("you can't go there. Go again.")


    board[position] = player

    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner

    row_winner = check_rows()
    columns_winner = check_columns()
    diagonals_winner = check_diagonals()
    if row_winner:
        winner = row_winner

    elif columns_winner:
        winner = columns_winner

    elif diagonals_winner:
        winner = diagonals_winner

    else:
        # no winner
        winner = None

def check_rows():
    global game_still_going
    # check if row has same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_3:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
    global game_still_going
    # check if row has same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

def check_diagonals():
    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    else:
        return None

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    global current_player

    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"


play_game()