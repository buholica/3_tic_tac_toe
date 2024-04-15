from tabulate import tabulate
from logo import logo
import random


POSITIONS_LIST = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
X_LETTER = 'X'
O_LETTER = 'O'

game_on = False
winner = None


def init_game():
    global winner, POSITIONS_LIST
    POSITIONS_LIST = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    winner = None


def checking_free_position(move, letter):
    """Checking is the position is free or not"""
    for row in POSITIONS_LIST:
        for index, position in enumerate(row):
            if position == move:
                if position == X_LETTER or position == O_LETTER:
                    return False
                else:
                    row[index] = letter
                    return True


def checking_results():
    """Checking results to finish or continue the game"""
    global winner

    # Checking the draw
    if all(position in [X_LETTER, O_LETTER] for row in POSITIONS_LIST for position in row):
        winner = 0

    # Checking results in a row
    for row in POSITIONS_LIST:
        result = all(position == row[0] for position in row)
        if result:
            for position in row:
                if position == X_LETTER:
                    winner = X_LETTER
                elif position == O_LETTER:
                    winner = O_LETTER

    # Checking results in a column
    transposed_list = list(zip(*POSITIONS_LIST))

    for col in transposed_list:
        if all(value == X_LETTER for value in col):
            winner = X_LETTER
        elif all(value == O_LETTER for value in col):
            winner = O_LETTER

    return winner


def announce_results(choice):
    global winner
    if winner == 0:
        return "It's a draw."
    elif winner == choice:
        return 'Congratulations, you won the game!'
    else:
        return 'You lose!'


def make_move(choice):
    """Asking a user to make a move"""
    user_move = int(input('Please, choose the position where you want to put X. '))
    if not checking_free_position(user_move, X_LETTER):
        print('Position is already occupied. Please choose another position.')
        user_move = int(input('Please, choose another position where you want to put X. '))


def computer_move(letter):
    """Asking computer to make a move"""
    pc_move = random.randint(1, 9)
    while not checking_free_position(pc_move, letter):
        pc_move = random.randint(1, 9)
    print(f'Computer move is {pc_move}.')
    print(tabulate(POSITIONS_LIST, tablefmt='pretty'))


def game(choice):
    global game_on
    if checking_results() == choice:
        print(announce_results(choice))
        game_on = False
    else:
        if choice == X_LETTER:
            make_move(user_choice)
        else:
            computer_move(X_LETTER)
            print(tabulate(POSITIONS_LIST, tablefmt='pretty'))

        if checking_results() == X_LETTER or checking_results() == O_LETTER or checking_results() == 0:
            print(tabulate(POSITIONS_LIST, tablefmt='pretty'))
            print(announce_results(choice))
            game_on = False
        else:
            if choice == 'O':
                make_move(user_choice)
            else:
                computer_move(O_LETTER)


print(logo)
user_input = input('Welcome to the Tic Tac Toe Game. \n'
                   'Please type "Start" to start the game or "Quit" to exit. ').lower()


if user_input == 'quite':
    print('Goodbye!')
elif user_input == 'start':
    user_choice = input("Please select 'X' or 'O': ").upper()
    game_on = True
    print(tabulate(POSITIONS_LIST, tablefmt='pretty'))
    while game_on:
        game(user_choice)

        if not game_on:
            restart = input("Do you want to restart the game? Type 'yes' or 'no'.\n").lower()
            if restart == 'no':
                print("It was nice to see you. Bye!!!")
                break
            else:
                init_game()
                user_choice = input("Please select 'X' or 'O': ").upper()
                print(tabulate(POSITIONS_LIST, tablefmt='pretty'))
                game_on = True