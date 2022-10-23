import random

def play_game():
    """
    a function to play the game
    """

    # call input_game() function and return the choices from user and computer
    user_choice, computer_choice = input_game()
    # compare the choices made by user
    winner(user_choice, computer_choice)


def int_game(num):
    """
    a function to convert int to string
        1: Rock
        2: Paper
        3: Scissor

    num: an integer from 1 to 3
    return: a text string
    """ 

    if num == 1:
        return 'Rock'
    elif num == 2:
        return 'Paper'
    elif num == 3:
        return 'Scissor'

def input_game():
    """
    a function to ask user to make a choice
    then, random generate an integer that stands for computer's choice
    """

    # user input
    user_input = int(input('Please Enter your choice (1 for Rock, 2 for Paper and 3 for Scissor): '))
    user_choice = int_game(user_input) # convert from int to text string
    
    # computer input
    computer_input = random.randint(1, 3)
    computer_choice = int_game(computer_input)

    # show choices made
    print('You show: ', user_choice)
    print('Computer shows: ', computer_choice)

    # return the choices as the output of this function
    return user_choice, computer_choice

def winner(user_choice, computer_choice):
    '''
    a function takes two inputs, compare and generate who is winner
    '''

    # if there was a tie
    if user_choice == computer_choice:
        # show message: tie
        print(f'Both players showed {user_choice}. It is a tie, one more round!')

        # re-play the game
        play_game()

    # if user chose Rock
    elif user_choice == 'Rock':
        
        # further to check computer's choice
        if computer_choice == 'Scissor':
            print('You win!')
        else:
            print('Computer Wins.')
    
    # if user chose Scissor
    elif user_choice == 'Scissor':
        if computer_choice == 'Paper':
            print('You win!')
        else:
            print('Computer Wins.')

    # if user choose Paper
    elif user_choice == 'Paper':
        if computer_choice == 'Rock':
            print('You win!')
        else:
            print('Computer Wins.')

# run the game
play_game()
