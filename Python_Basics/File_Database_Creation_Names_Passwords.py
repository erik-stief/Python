# Name: Erik Stiefeling
# Date: November 20, 2024
# Description: A program to create a table of different 
# user names and passwords. The user inputs user names and the program 
# validates whether the input is acceptable. The program then 
# generates a password for the user and stores both the user names and 
# passwords into a CSV file. The program then reads from the file to 
# output the data into a readable table.

import random 

# takes 1 argument, file_name (string)
# tries to open a file named after the file_name string
# if one exists it truncates it
# and if it doesn't exist it creates a new file
# and returns True
# if an exeption occurs it returns False
def create_db(file_name):
    try:
        with open(file_name, 'w') as myfile:
            return True
    except:
        return False

# takes 1 argument, file_name (string)
# reads the CSV file named after the file_name string
# sorts the values into two lists named names and passwords
# and returns the lists
# if an exeption occurs it returns two Nones
def read_users(file_name):
    names = []
    passwords = []
    try:
        with open(file_name, 'r') as myfile:
            for line in myfile:
                names.append(line.split(',')[0])
                passwords.append(line.rstrip('\n').split(',')[1])
        return names, passwords
    except:
        return None, None

# takes 2 arguments, names and passwords (strings)
# if the names argument is empty it displays No user found
# else it displays the names and passwords lists in a chart
def display_users(names, passwords):
    if names == []:
        print('No user found')
    else:
        print(f'{'No.':<5}{'Name':<20}Password')
        print('-' * 35)
        count = 0
        for name in names:
            print(f'{count + 1:<5}{name:<20}{passwords[count]}')
            count+=1

# takes 1 argument, name (string)
# Checks if the length of name is greater or equal to 3
# and if name only contains letters
# returns True if the above conditions hold
# and False if they don't
def valid_name(name):
    if len(name) >= 3 and name.isalpha():
        return True
    else:
        return False

# takes 1 argument, name (string)
# Appends the first character of name to password
# Appends the length of name to password
# Generates 6 random charcters using a while loop and appends them to password
# and returnes a string containing the generated password
def generate_password(name):
    password = ''
    password = name[0]
    password = password + str(len(name))
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = lower_case.upper()
    digits = '0123456789'
    special_char = '+-*/_#$'
    password_options = lower_case + upper_case + digits + special_char
    count = 0
    while count < 6:
        password = password + random.choice(password_options)
        count +=1
    return password

# takes 1 argument, file_name (string)
# repeats taking input from the user until "s" (meaning stop)
# calls valid_name function to validate the user name 
# if the user name is invalid it prints the message "Name is invalid"
# if the name already exits it prints the message "Name already Exists"
# otherwise calls the generate_password to generate a password for the user
# the function then writes the user names and passwords to a file in CSV format
# after signing up all the user names it returns the number of all users 
# in the file or return -1 if any exceptions arise
def sign_up(file_name):
    try:
        name = ''
        name_check = []
        count = 0
        with open(file_name, 'r') as myfile:
            while name != 's':
                name = input('Enter name (\'s\' to Stop): ')
                if name == 's':
                    break
                elif valid_name(name) == False:
                    print('Name is invalid.')
                elif name in name_check:
                    print('Name already Exists.')
                else:
                    password = generate_password(name)
                    name_check.append(name.split(',')[0])
                    count += 1
                    print(f'Hello {name}, your password is: {password}')
                    with open(file_name, 'a') as myfile:
                        myfile.write(f'{name},{password}\n')
        return count
    except:
        return -1


def change_password(file_name, name, new_password): # Both
    # TODO 7/7
    pass


USER_DB = 'assignment3_lastname.csv'

# == DO NOT MODIFY ANY CODE BELOW THIS LINE ==

def main(): 
    print('Create DB:', create_db(USER_DB)) # Create DB: True
    names, passwords = read_users(USER_DB)
    display_users(names, passwords)  # No user found

    print('Count:', sign_up(USER_DB))
    names, passwords = read_users(USER_DB)
    display_users(names, passwords)

    print('Change first name:',      # Change first name: True
          change_password(USER_DB, names[0], 
                          generate_password(names[0]))) 
    print('Change last name: ',      # Change last name: True
          change_password(USER_DB, names[len(names) - 1], 
                          generate_password(names[len(names) - 1])))
    print('Change dumb name: ',      # Change dumb name: False
          change_password(USER_DB, 'ProfSun', # Username does not exist
                          generate_password('ProfSun'))) 

    names, passwords = read_users(USER_DB)
    display_users(names, passwords)
    
if __name__ == '__main__':
    main()