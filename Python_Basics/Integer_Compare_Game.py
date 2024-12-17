# Name: Erik Stiefeling
# Date: September 17, 2024
# Description: Takes 2 positive integers and compares them.
# Then the program finds and prints the common factors between the 2 integers.
# Finally it asks the user if they would like to play again;
# and replays the program if the answer is 'Y' or 'y'.

play_again = 'y'
while (play_again == 'y' or play_again == 'Y'):
    
    # Asks the user to enter the first positive integer and 
    # checks if the value entered is a positive integer
    # Using a while loop to make sure inputs are valid.
    num_1_count = 0
    while (num_1_count == 0):
        num_1 = int(input('= Enter the first positive integer: '))
        if (num_1 > 0):
            num_1_count = 1
        else:
            print('Error: number must be positive.')

    # Asks the user to enter the second positive integer and 
    # checks if the value entered is a positive integer
    # Using a while loop to make sure inputs are valid.
    num_2_count = 0
    while (num_2_count == 0):    
        num_2 = int(input('= Enter the second positive integer: '))
        if (num_2 > 0):
            num_2_count = 1
        else:
            print('Error: number must be positive.')

    # Compares the 2 positive integers 
    # and prints a statement detailing how the comparison went.
    if (num_1 > num_2):
        print(f'= {num_1} is greater than {num_2}')
    elif (num_1 < num_2):
        print(f'= {num_1} is less than {num_2}')
    else:
        print('The two numbers are equal')

    # Loops through a range up to num_1
    # Adds 1 to fact to make sure the range goes up to num_1.
    # Uses modulus to find the common factors between num_1 and num_2.
    common_factor = ''
    for fact in range(num_1):
        factor = fact+1
        if num_1 % factor == 0 and num_2 % factor == 0:
            if common_factor == '':
                common_factor = f'{factor}'
            else:
                common_factor = f'{common_factor}, {factor}'
    print(f'= Common factors of {num_1} and {num_2} are: {common_factor}')

    # Asks user if they would like to use the program again.
    # Checks to make sure the users input is one of the 4 valid options.
    # Using a while loop to make sure inputs are valid.
    play_again = input('= Play again? (Y/N or y/n): ')
    play_again_count = 0
    while (play_again_count < 1):
        if (play_again == 'Y' or play_again == 'y' 
            or play_again == 'N' or play_again == 'n'):
            play_again_count = 1
        else:
            print('Error: choice must be (Y/N) or (y/n).')
            play_again = input('= Play again? (Y/N or y/n): ')