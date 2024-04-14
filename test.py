from tabulate import tabulate
from logo import logo
import random

POSITIONS_LIST = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x_letter = 'X'
o_letter = 'O'

def init_game():
    global POSITIONS_LIST, winner
    POSITIONS_LIST = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    winner = None

def checking_free_position(move, letter):
    """Checking if the position is free or not"""
    for row in POSITIONS_LIST:
        if move in row:
            index = row.index(move)
            if row[index] not in [x_letter, o_letter]:
                row[index] = letter
                return True
    return False

def checking_results():
    """Checking results to finish or continue the game"""
    global winner

    if all(position in [x_letter, o_letter] for row in POSITIONS_LIST for position in row):
        winner = 2

    for row in POSITIONS_LIST:
        if all(position == row[0] for position in row):
            winner = 1 if row[0] == x_letter else 0

    transposed_list = list(zip(*POSITIONS_LIST))
    for col in transposed_list:
        if all(position == col[0] for position in col):
            winner = 1 if col[0] == x_letter else 0

    return winner

def announce_results():
    if winner == 1:
        return 'Congratulations, you won the game!'
    elif winner == 0:
        return 'You lose!'
    else:
        return "It's a draw."

def game():
    global winner
    user_move = int(input('Please, choose the position where you want to put X. '))
    if not checking_free_position(user_move, x_letter):
        print('Position is already occupied. Please choose another position.')
        return

    winner = checking_results()
    if winner is not None:
        print(tabulate(POSITIONS_LIST, tablefmt='pretty'))
        print(announce_results())
        return

    computer_move = random.randint(1, 9)
    while not checking_free_position(computer_move, o_letter):
        computer_move = random.randint(1, 9)
    print(f'Computer move is {computer_move}.')
    print(tabulate(POSITIONS_LIST, tablefmt='pretty'))

print(logo)
user_input = input('Welcome to the Tic Tac Toe Game.\n'
                   'Please type "Start" to start the game or "Quit" to exit. ').lower()

if user_input == 'start':
    while True:
        init_game()
        print(tabulate(POSITIONS_LIST, tablefmt='pretty'))
        while not checking_results():
            game()
        restart = input("Do you want to restart the game? Type 'yes' or 'no'.\n").lower()
        if restart == 'no':
            print("Goodbye!")
            break
elif user_input == 'quit':
    print('Goodbye!')

