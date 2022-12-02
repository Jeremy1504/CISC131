import tkinter
from tkinter import Label, Entry, Text, StringVar, Button, END
'''
A simple example to wrap a password generator in a GUI app.
'''
def generatePassword(n):
    '''
    need to modify
    use 'hello world' for place-holder
    '''
    return 'hello world ' * n


def main():
    # create a Tk() window
    window = tkinter.Tk()
    # set title
    window.title("Password Generator")

    # Creating Label widgets
    input_label = Label(window, text = "Enter a number")
    # Create a StringVar()
    value = StringVar()
    # input box
    input_value = Entry(window, textvariable = value)
    # output label
    output_label = Label(window, text = 'Result')

    # grid alignment
    input_label.grid(row = 0, column = 0, padx=10, pady=10)
    input_value.grid(row = 0, column = 1, pady=10, padx=10)
    output_label.grid(row = 4, column = 0, pady=10, padx=10)

    # Creating Text Widget as output value
    output_text = Text(window, height = 1, width = 30)

    def trigger_function():
        # call function to calculate
        result = generatePassword(int(value.get()))
        # clear content (startIndex, endIndex)
        output_text.delete("1.0", END)
        # update results (index, String)
        output_text.insert(END, result)

    # Creating Button Widget
    button_convert = Button(window, text = "Click", command = trigger_function)
    
    # grid alignment
    output_text.grid(row = 4, column = 1, pady=10, padx=10)
    button_convert.grid(row = 1, column = 1, padx=10, pady=10)

    # exit button
    button_quit = Button(window, text="Quit", command=window.destroy) 

    window.mainloop()

main()