import os


def greeter():  # !
    print("T I C T A C T O E\n  W E L C O M E")
    start_key = input('Press any key to continue')
    if start_key == '':
        pass
    else:
        pass
        # os.system("pause")


def play_again():  # !
    new_game = True
    user_Input = input('Fancy a new game? Y/N\n')

    while new_game:
        if user_Input.upper() == 'Y':
            main()
        elif user_Input.upper() == 'N':
            print('Thank you for playing!!')
            break
        else:
            print('Please enter a valid input.')


def full_board(board_list):  # !
    if board_list[0] and board_list[1] and board_list[2] and board_list[3] \
            and board_list[4] and board_list[5] and board_list[6] \
            and board_list[7] and board_list[8] not in ' ':
        print('Tie!!')

        return True

    return False


def print_board(board_list):  # !
    print('\n'*100)
    print('||'+board_list[0]+'||'+board_list[1]+'||'+board_list[2]+'||')
    print('||~||~||~||')
    print('||'+board_list[3]+'||'+board_list[4]+'||'+board_list[5]+'||')
    print('||~||~||~||')
    print('||'+board_list[6]+'||'+board_list[7]+'||'+board_list[8]+'||')


def pick_player(p1, p2):  # !

    p1 = ''
    p2 = ''
    marker = ''
    while True:

        player_choice = input(
            'Please choose your player marker (X or O) to start:')

        if player_choice.upper() == 'X':
            p1 = 'X'
            p2 = 'O'
            print("Player 1:'X'\nPlayer 2: 'O'\nPress Enter to continue")
            input()

        elif player_choice.upper() == 'O':
            p1 = 'O'
            p2 = 'X'
            print("Player 1:'O'\nPlayer 2: 'X'\nPress any key to continue")
            input()

        else:
            print('Invalid input, try again')
            continue

        return p1, p2


def game_logic(p1, p2, board_list):  # !
    game_on = True
    while game_on:

        pl_pos = input('Player 1, select your position on the board (1-9):\n')

        if pl_pos not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print('Please enter a valid input (1-9):\n')
        else:
            p1_int_pos = int(pl_pos) - 1

        if board_list[p1_int_pos] == p1 or board_list[p1_int_pos] == p2:
            print("Cannot overwrite already marked field. Try again")
        else:
            board_list[p1_int_pos] = p1

        print_board(board_list)

        if board_list[0] == board_list[1] == board_list[2] == p1 or \
                board_list[3] == board_list[4] == board_list[5] == p1 or \
                board_list[6] == board_list[7] == board_list[8] == p1:
            print('Player 1 won!')
            game_on == False
            break

        elif board_list[0] == board_list[3] == board_list[6] == p1 or \
                board_list[1] == board_list[4] == board_list[7] == p1 or \
                board_list[2] == board_list[5] == board_list[8] == p1:
            print('Player 1 won!')
            game_on == False
            break

        elif board_list[0] == board_list[4] == board_list[8] == p1 or \
                board_list[2] == board_list[4] == board_list[6] == p1:
            print('Player 1 won!')
            game_on == False
            break

        pl_pos = input(
            'Player 2, Select your position in the board (0-8): ')

        if pl_pos not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print('Please enter a valid input (1-9):\n')
        else:
            p2_int_pos = int(pl_pos) - 1

        if board_list[p2_int_pos] == p1 or board_list[p2_int_pos] == p2:
            print("Cannot overwrite already marked field. Try again")
        else:
            board_list[p2_int_pos] = p2

        print_board(board_list)

        if board_list[0] == board_list[1] == board_list[2] == p2 or \
                board_list[3] == board_list[4] == board_list[5] == p2 or \
                board_list[6] == board_list[7] == board_list[8] == p2:
            print('Player 2 won!')
            game_on == False
            break

        elif board_list[0] == board_list[3] == board_list[6] == p2 or \
                board_list[1] == board_list[4] == board_list[7] == p2 or \
                board_list[2] == board_list[5] == board_list[8] == p2:
            print('Player 2 won!')
            game_on == False
            break

        elif board_list[0] == board_list[4] == board_list[8] == p2 or \
                board_list[2] == board_list[4] == board_list[6] == p2:
            print('Player 2 won!')
            game_on == False
            break

        if full_board(board_list):
            game_on = False
            break


def main():  # !
    p1 = ''
    p2 = ''
    board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]

    p1, p2 = pick_player(p1, p2)
    print_board(board_list)
    game_logic(p1, p2, board_list)
    play_again()


greeter()
main()
