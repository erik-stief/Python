# Name: Erik Stiefeling
# Date: October 13, 2024
# Description: The main program that is used to call the helper functions
# and uses their returned values to play the game

# Imports helper functions from different python script
from Helper_Function_Dice_Game import valid_number_check, dice_roll, print_format

# Main function to run the dice rolling game.
# Prompts the user for the number of dice rolls
# using helper functions to simulate dice rolls
# Takes no arguments
def main():
    run_game = 0
    while run_game == 0:
        rolling_times = valid_number_check(1,
                                            10000,
                                            'Rolling Times (1-10000, 0 to stop) : ',
                                            'Invalid number')
        if rolling_times == 0:
            print('Thank you')
            break;
        else:
            one, two, three, four, five, six = dice_roll(rolling_times)
            max_roll = max(one, two, three, four, five, six)
            print()
            print_format('One  ', round(70*one/max_roll), '=', one)
            print_format('Two  ', round(70*two/max_roll), '=', one)
            print_format('Three', round(70*three/max_roll), '=', three)
            print_format('Four ', round(70*four/max_roll), '=', four)
            print_format('Five ', round(70*five/max_roll), '=', five)
            print_format('Six  ', round(70*six/max_roll), '=', six)
            print()

# Entry point to start the main function
main()
