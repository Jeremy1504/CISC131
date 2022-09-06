import random

def play_game():
    user_choice, computer_choice = input_game()
    winner(user_choice, computer_choice)

# a function to convert int to string
def int_game(num):
    if num == 1:
        return 'Rock'
    elif num == 2:
        return 'Paper'
    elif num == 3:
        return 'Scissor'

def input_game():
    user_input = int(input('Please Enter your choice (1 for Rock, 2 for Paper and 3 for Scissor): '))
    user_choice = int_game(user_input)

    computer_input = random.randint(1, 3)
    computer_choice = int_game(computer_input)

    print('You show: ', user_choice)
    print('Computer shows: ', computer_choice)

    return user_choice, computer_choice

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f'Both players showed {user_choice}. It is a tie, one more round!')
        play_game()

    elif user_choice == 'Rock':
        if computer_choice == 'Scissor':
            print('You win!')
        else:
            print('Computer Wins.')
    
    elif user_choice == 'Scissor':
        if computer_choice == 'Paper':
            print('You win!')
        else:
            print('Computer Wins.')

    elif user_choice == 'Paper':
        if computer_choice == 'Rock':
            print('You win!')
        else:
            print('Computer Wins.')

play_game()
