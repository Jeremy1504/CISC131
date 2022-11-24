import random

import tkinter
from tkinter import Label, Entry, Text, StringVar, Button, END
'''
A simple example to wrap a password generator in a GUI app.
'''
def generatePassword(n):
    '''
    A simple function to generate strong password in a given length
    - n: length of passowrd
    - output: return the password 
    '''
    # input validation
    # length should be at least 8 characters
    if n < 8:
       raise ValueError()
       return 0

    else:
        # character set
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = lower.upper()
        num = '1234567890'
        symbol = '~!@#$%^&*_-+=`|\(){}[]:;<>,.?/'
        # a long string that contains all candidate characters
        random_source = lower + upper + num + symbol

        password = ''
        # pick at least one character from the candidate set
        # pick at least one lower, one upper, one number, one special character
        password += random.choice(lower)
        password += random.choice(upper)    
        password += random.choice(num)
        password += random.choice(symbol)

        # fill in the rest of the characters
        for i in range(n - 4):
            password += random.choice(random_source)

        # shuffle only works on a list
        password_lst = list(password)
        random.shuffle(password_lst)
        
        # convert list back to string
        return ''.join(password_lst)


def main():

    window = tkinter.Tk()
    # set title
    window.title("Password Generator")

    # Creating Label widgets
    input_label = Label(window, text = "Enter the length of password")
    # Create a StringVar()
    value = StringVar()

    input_value = Entry(window, textvariable = value)
    output_label = Label(window, text = 'Result')

    # grid alignment
    input_label.grid(row = 0, column = 0, padx=10, pady=10)
    input_value.grid(row = 0, column = 1, pady=10, padx=10)
    output_label.grid(row = 4, column = 0, pady=10, padx=10)

    # Creating Text Widgets
    output_text = Text(window, height = 1, width = 30)

    def trigger_function():
        result = generatePassword(int(value.get()))
        output_text.delete("1.0", END)
        output_text.insert(END, result)

    # Creating  Button Widget
    button_convert = Button(window, text = "Generate", command = trigger_function)
    
    # grid alignment
    output_text.grid(row = 4, column = 1, pady=10, padx=10)
    button_convert.grid(row = 1, column = 1, padx=10, pady=10)

    # exit button
    button_quit = Button(window, text="Quit", command=window.destroy) 
    # # button position
    # button_quit.place(x=450,y=255)

    window.mainloop()

main()