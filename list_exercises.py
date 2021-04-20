def get_numbers():
    """ask the user to input 5 numbers"""
    num_list = []
    for x in range(5):
        valid_input = False
        while not valid_input:
            try:
                number = float(input("Number: "))
                num_list.append(number)
                valid_input = True
            except ValueError:
                print("Please enter a number!")
    print(f"The first number is {num_list[0]}")
    print(f"The last number is {num_list[-1]}")
    print(f"The smallest number is {min(num_list)}")
    print(f"The largest number is {max(num_list)}")
    print(f"The average of the numbers is {sum(num_list)/len(num_list)}")


def username_check():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    get_username = input("Enter username: ")
    if get_username in usernames:
        print("Access granted")
    else:
        print("Access denied")


username_check()