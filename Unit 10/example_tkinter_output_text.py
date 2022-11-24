import tkinter
from tkinter import Label, Entry, Text, StringVar, Button, END
'''
A simple example to create an length converter with Text output
- grid alignment
- text can be copied and pasted
'''
def main():

    window = tkinter.Tk()
    # set title
    window.title("Lenghth Converter")
    # set window size
    # window.geometry("500x300+550+355")

    # Creating Label widgets
    input_label = Label(window, text = "Enter a length in centimeters")
    # Create a StringVar()
    value = StringVar()

    input_value = Entry(window, textvariable = value)
    output_label = Label(window, text = 'Result')

    # grid alignment
    input_label.grid(row = 0, column = 0, padx=10, pady=10)
    input_value.grid(row = 0, column = 1, pady=10, padx=10)
    output_label.grid(row = 4, column = 0, pady=10, padx=10)

    # Creating Text Widgets
    output_text = Text(window, height = 1, width = 15)

    def convert_cm():
        result = round(float(value.get())/2.54, 2)   
        output_text.delete("1.0", END)
        output_text.insert(END, result)

    # Creating  Button Widget
    button_convert = Button(window, text = "Converted to inches", command = convert_cm)
    
    # grid alignment
    output_text.grid(row = 4, column = 1, pady=10, padx=10)
    button_convert.grid(row = 1, column = 1, padx=10, pady=10)

    # exit button
    button_quit = Button(window, text="Quit", command=window.destroy) 
    # button position
    button_quit.place(x=450,y=255)

    window.mainloop()

main()