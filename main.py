from tabulate import tabulate
from logo import logo
import random


POSITIONS_LIST = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
game_on = False
winner = None
x_letter = 'X'
o_letter = 'O'

print(logo)
user_input = input('Welcome to the Tic Tac Toe Game. \n'
                   'Please, type "Start" to start the game. ').lower()


def init_game():
    global winner, POSITIONS_LIST
    POSITIONS_LIST = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    winner = None


def checking_free_position(move, letter):
    """Checking is the position is free or not"""
    for row in POSITIONS_LIST:
        for index, position in enumerate(row):
            if position == move:
                if position == x_letter or position == o_letter:
                    return False
                else:
                    row[index] = letter
                    return True


def checking_results():
    """Checking results to finish or continue the game"""
    global winner

    if all(position == x_letter or position == o_letter for row in POSITIONS_LIST for position in row):
        winner = 2

    # Checking results in a row
    for row in POSITIONS_LIST:
        result = all(position == row[0] for position in row)
        if result:
            for position in row:
                if position == x_letter:
                    winner = 1
                elif position == o_letter:
                    winner = 0


    # Checking results in a column
    transposed_list = list(zip(*POSITIONS_LIST))

    x_in_f_col = all(value == x_letter for value in transposed_list[0])
    x_in_s_col = all(value == x_letter for value in transposed_list[1])
    x_in_th_col = all(value == x_letter for value in transposed_list[2])

    o_in_f_col = all(value == o_letter for value in transposed_list[0])
    o_in_s_col = all(value == o_letter for value in transposed_list[1])
    o_in_th_col = all(value == o_letter for value in transposed_list[2])

    if x_in_f_col or x_in_s_col or x_in_th_col:
        winner = 1
    elif o_in_f_col or o_in_s_col or o_in_th_col:
        winner = 0

    return winner


def announce_results():
    global winner
    if winner == 1:
        return 'Congratulations, you won the game!'
    elif winner == 0:
        return 'You lose!'
    else:
        return "It's a draw."


def game():
    global game_on
    if checking_results() == 0:
        print(announce_results())
        game_on = False
    else:
        user_move = int(input('Please, choose the position where you want to put X. '))
        if not checking_free_position(user_move, x_letter):
            print('Position is already occupied. Please choose another position.')
            user_move = int(input('Please, choose another position where you want to put X. '))

        if checking_results() == 1 or checking_results() == 2 or checking_results() == 0:
            print(tabulate(POSITIONS_LIST, tablefmt='pretty'))
            print(announce_results())
            game_on = False
        else:
            computer_move = random.randint(1, 9)
            while not checking_free_position(computer_move, o_letter):
                computer_move = random.randint(1, 9)
            print(f'Computer move is {computer_move}.')
            print(tabulate(POSITIONS_LIST, tablefmt='pretty'))


if user_input == 'quite':
    print('Goodbye!')
elif user_input == 'start':
    game_on = True
    print(tabulate(POSITIONS_LIST, tablefmt='pretty'))
    while game_on:
        game()

        if not game_on:
            restart = input("Do you want to restart the game? Type 'yes' or 'no'.\n").lower()
            if restart == 'no':
                print("It was nice to see you. Bye!!!")
                break
            else:
                init_game()
                print(tabulate(POSITIONS_LIST, tablefmt='pretty'))
                game_on = True