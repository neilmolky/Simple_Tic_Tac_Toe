# Simple Tic-tac-toe
# an unfinished programme by neilmolky for jetbrains academy
# https://hyperskill.org/
# after I completed the project I wanted to see if it was possible to
# add AI for a single player mode.
# logic is present in comments but I want to change the working of
# the co-ordinates to be able to measure vectors first as the logic for the AI
# includes working out distance on turn 3 and 4 to inform the decision tree

import random

# create an empty string to serve as a starting variable for our blank board
init_state = "         "
# convert this into a list that will be our global variable for board state
board_state = []
for char in init_state:
    board_state.append(char)
# convert the list back to a string to be read for win conditions
win_con = "".join(board_state)

# create a function to print board. within this function you can better visualise
# how the index matches up to its position in our board matrix


def print_board():
    global board_state
    board_matrix = [                                       # x,y (x * 3) + (y - 4)
        [board_state[0], board_state[1], board_state[2]],  # 1,1, 1,2, 1,3
        [board_state[3], board_state[4], board_state[5]],  # 2,1, 2,2, 2,3
        [board_state[6], board_state[7], board_state[8]]   # 3,1, 3,2, 3,3
    ]
    # show the board
    print("---------")
    for row in board_matrix:
        print("| ", end="")
        print(*row, end="")
        print(" |")
    print("---------")

# create a function to change the board state
# to translate the coordinate value to the index value of board_state string use equation
# board_state_index = (x * 3) + (y - 4)


def player_move(x_pos, y_pos, x_or_o):
    global board_state
    global invalid_move
    string_index = int(x_pos * 3) + (y_pos - 4)
    if board_state[string_index] == ' ':
        invalid_move = False
        board_state[string_index] = x_or_o
    else:
        invalid_move = True


def program_move(index, x_or_o):
    global board_state
    board_state[index] = x_or_o


# at the start of the programme print the empty board. Later this will be updated
print_board()

# The below variables help control the in game loop and return messages
# when the wrong co-ordinates are entered by a user.
# Turn will be used to play the computer.
invalid_coord = True
invalid_move = True
running = True
turn = 0
players = 1
player_turn = random.choice([1, 2])
playing_piece = random.choice(["X", "O"])
if playing_piece == "X":
    program_piece = "O"
else:
    program_piece = "X"

add_player = input("press y to add a second player. any other key will play the program:")
if add_player == "y":
    players += 1

while running is True:
    if players == 2:
        coordinates = []
        player_turn_input = input("Enter the coordinates:").split()
        for n in player_turn_input:
            if n.isnumeric():
                if 0 <= int(n) <= 3:
                    coordinates.append(int(n))
                    invalid_coords = False
                else:
                    invalid_coords = True
                    print("Coordinates should be from 1 to 3!")
                    break
            else:
                invalid_coords = True
                print("You should enter numbers!")
                break

        if invalid_coords is False:
            if win_con.count("X") == 0:
                player_turn = "X"
            elif win_con.count("X") > win_con.count("O"):
                player_turn = "O"
            else:
                player_turn = "X"
            player_move(coordinates[0], coordinates[1], player_turn)
            if invalid_move:
                print("This cell is occupied! Choose another one!")
            else:
                print_board()
                win_con = "".join(board_state)
# Basic AI
    else:
        coordinates = []
        turn += 1
        if player_turn == 1:
            print("you go first!")
            player_turn = True
        elif player_turn == 2:
            print("I'll go first!")
            player_turn = False
            program_goes_first = random.randint(0, 8)
        elif player_turn:
            player_turn_input = input("Enter the coordinates:").split()
            for n in player_turn_input:
                if n.isnumeric():
                    if 0 <= int(n) <= 3:
                        coordinates.append(int(n))
                        invalid_coords = False
                    else:
                        invalid_coords = True
                        print("Coordinates should be from 1 to 3!")
                        break
                else:
                    invalid_coords = True
                    print("You should enter numbers!")
                    break
            player_turn = False
        elif not player_turn:
            # Logic for computer to win or draw
            if turn == 1:
                program_move(program_goes_first, program_piece)
            elif turn == 2:
                if win_con.find(playing_piece) == 4:  # player chose middle
                    # program chooses a corner
                    program_move(random.choice([0, 2, 6, 8]), program_piece)
                if win_con.find(playing_piece) % 2 == 1:  # player chose side
                    # program chooses middle
                    program_move(4, program_piece)
                else:  # player chose corner
                    # program chooses opposite corner
                    if win_con.find(playing_piece) == 0:
                        program_move(8, program_piece)
                    elif win_con.find(playing_piece) == 2:
                        program_move(6, program_piece)
                    elif win_con.find(playing_piece) == 6:
                        program_move(2, program_piece)
                    else:
                        program_move(0, program_piece)
            elif turn == 3:
                pass
                # if player piece is within 1 square of program piece
                # prioritise play next to existing program piece
                # in a corner or if program piece is in the corner in the middle
                # or if player piece is in the middle program will draw

                # if player piece is not within 1 square of playing piece
                # program chooses farthest corner from itself,
                # if occupied choose center
            elif turn >= 4:
                pass
                # check if this turn win is possible and execute
                # if win not possible check for win threat and block,
                # if no win threat make mid edge corner close formation for guaranteed win
                # if mid edge corner formation blocked play until draw choose random remaining square

            invalid_coords = False
            player_turn = True

        if invalid_coords is False:
            if win_con.count("X") == 0:
                player_turn = "X"
            elif win_con.count("X") > win_con.count("O"):
                player_turn = "O"
            else:
                player_turn = "X"
            player_move(coordinates[0], coordinates[1], player_turn)
            if invalid_move:
                print("This cell is occupied! Choose another one!")
            else:
                print_board()
                win_con = "".join(board_state)
    # store win conditions as a list of booleans
    # Win conditions are calculated from player input rather than the board matrix.
    # iterating over the string using the [start: end: jump] function
    # calculate if true and store the boolean values as a list

    x_wins = [
        # Horizontal wins
        win_con[0: 3] == "XXX",
        win_con[3: 6] == "XXX",
        win_con[6: 9] == "XXX",
        # Vertical wins
        win_con[0: 9: 3] == "XXX",
        win_con[1: 9: 3] == "XXX",
        win_con[2: 9: 3] == "XXX",
        # Diagonal wins
        win_con[0: 9: 4] == "XXX",
        win_con[2: 8: 2] == "XXX"
        ]

    o_wins = [
        # Horizontal wins
        win_con[0: 3] == "OOO",
        win_con[3: 6] == "OOO",
        win_con[6: 9] == "OOO",
        # Vertical wins
        win_con[0: 9: 3] == "OOO",
        win_con[1: 9: 3] == "OOO",
        win_con[2: 9: 3] == "OOO",
        # Diagonal wins
        win_con[0: 9: 4] == "OOO",
        win_con[2: 8: 2] == "OOO"
        ]

    # Valid game outcomes
    if True in x_wins:
        running = False
        print("X wins")
    elif True in o_wins:
        running = False
        print("O wins")
    elif win_con.count("X") >= 5:
        running = False
        print("Draw")

