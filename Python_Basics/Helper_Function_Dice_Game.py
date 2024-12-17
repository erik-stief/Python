# Name: Erik Stiefeling
# Date: October 13, 2024
# Description: A group of helper functions that are used to help another python script
# run a dice simulation game.

import random # Imports random module to generate random numbers

# Prompts the user for a number within specified bounds 
# until a valid input is received. 
# Takes 4 arguments, 
# a lower bound (int), upper bound (int),
# a prompt message (str), and a error message(str)
# and returns a number with the specidfied range 
# or 0 if the user wants to end the program
def valid_number_check(lower_bound, upper_bound, prompt_message, error_message):
    check_roll = 0
    while check_roll == 0:
        rolling_times = int(input(prompt_message))
        if rolling_times == 0:
            return 0
        elif rolling_times < lower_bound or rolling_times > upper_bound:
            print(error_message)
        else:
            return rolling_times

# Simulates rolling a dice a specified number of times 
# and counts the occurrences of each face.
# takes 1 argument, rolling_times (int)
# and returnes a tuple conaining counts of each dice face      
def dice_roll(rolling_times):
    one, two, three, four, five, six  = 0,0,0,0,0,0
    for roll in range(rolling_times):
        roll_result = random.randint(1,6)
        if roll_result == 1:
            one += 1
        elif roll_result == 2:
            two += 1
        elif roll_result == 3:
            three += 1
        elif roll_result == 4:
            four += 1
        elif roll_result == 5:
            five += 1
        else:
            six += 1
    return one, two, three, four, five, six


# Prints a formatted string with a title, a line of repeated characters, and a note.
# takes 4 arguments,
# title (str), length (int), character (str), and note (str)
def print_format(title, length, character, note):
    full_character = ''
    for char in range(length):
        if full_character == '':
            full_character = character
        else:
            full_character = f'{full_character}{character}'
    print(f'{title}: {full_character} {note}')