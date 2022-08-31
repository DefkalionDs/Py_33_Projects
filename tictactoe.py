import os


def winner_check(pl_name, pl_choice, board_list):

    if board_list[0] == board_list[1] == board_list[2] == pl_choice or \
            board_list[3] == board_list[4] == board_list[5] == pl_choice or \
            board_list[6] == board_list[7] == board_list[8] == pl_choice:
        print(f'{pl_name} won!')
        return True

    elif board_list[0] == board_list[3] == board_list[6] == pl_choice or \
            board_list[1] == board_list[4] == board_list[7] == pl_choice or \
            board_list[2] == board_list[5] == board_list[8] == pl_choice:
        print(f'{pl_name} won!')
        return True

    elif board_list[0] == board_list[4] == board_list[8] == pl_choice or \
            board_list[2] == board_list[4] == board_list[6] == pl_choice:
        print(f'{pl_name} won!')
        return True


def player_turns(p1, p2, marker, board_list, pl_pos, game_on):

    if marker.upper() != p1 != p2:
        pl_name = 'Player 1'
        marker = p1
        pl_choice = p1
    elif marker.upper() != p1:
        pl_name = 'Player 1'
        marker = p1
        pl_choice = p1
    elif marker.upper() != p2:
        pl_name = 'Player 2'
        marker = p2
        pl_choice = p2

    pl_pos = input(
        f'{pl_name}, select your position on the board (1-9):\n')

    while pl_pos not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print('Please enter a valid input (1-9):\n')
        pl_pos = input()

    else:
        pl_int_pos = int(pl_pos) - 1

    while board_list[pl_int_pos] == p1 or board_list[pl_int_pos] == p2:
        print("Cannot overwrite already marked field. Try again.\n")
        pl_int_pos = int(input()) - 1

    else:
        board_list[pl_int_pos] = pl_choice

    print_board(board_list)


def greeter():
    
    print("T I C T A C T O E\n  W E L C O M E")
    start_key = input('Press any key to continue')
    if start_key == '':
        pass
    else:
        pass


def play_again():
    
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
            user_Input = input().upper()
    os._exit(1)


def full_board(board_list):

    if board_list.count(' ') <= 0:
        print("Tie!!")
        return True
    else:
        return False


def print_board(board_list):
    
    print('\n'*100)
    print('||'+board_list[0]+'||'+board_list[1]+'||'+board_list[2]+'||')
    print('||~||~||~||')
    print('||'+board_list[3]+'||'+board_list[4]+'||'+board_list[5]+'||')
    print('||~||~||~||')
    print('||'+board_list[6]+'||'+board_list[7]+'||'+board_list[8]+'||')


def pick_player(p1, p2):

    p1 = ''
    p2 = ''

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


def game_logic(p1, p2, board_list):
    
    marker = ''
    pl_pos = ''
    pl_choice = ''
    pl_name = ''
    game_on = True
    while game_on:

        player_turns(p1, p2, marker, board_list, pl_pos, game_on)

        if pl_name == 'Player 1':
            pl_name = 'Player 2'
        else:
            pl_name = 'Player 1'

        if pl_choice == p1:
            pl_choice = p2
        else:
            pl_choice = p1

        if winner_check(pl_name, pl_choice, board_list):
            game_on = False
            break

        if full_board(board_list):
            game_on = False
            break

        if marker == p1:
            marker = p2
        else:
            marker = p1


def main():
    
    p1 = ''
    p2 = ''
    board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]

    p1, p2 = pick_player(p1, p2)
    print_board(board_list)
    game_logic(p1, p2, board_list)
    play_again()


greeter()
main()
