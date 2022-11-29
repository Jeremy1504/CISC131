import tkinter
import tkinter.messagebox # import messagebox moudule

def main():
    window = tkinter.Tk()

    # create label and user's input box
    user_input_label = tkinter.Label(window, text = 'Enter a length in centimeters: ')
    user_input_value = tkinter.Entry(window, width = 10)
    
    user_input_label.pack(side = 'left')
    user_input_value.pack(side = 'left')

    # Create the widgets for result
    result_label = tkinter.Label(window, text = 'Converted to inches: ')

    # create a StringVar object and store a string of blank char.
    value = tkinter.StringVar(window, 0)
    # Create a label and associate it with the StringVar object.
    # its value will be stored in StringVar object will automatically be displayed in the label
    output_label = tkinter.Label(window, textvariable = value, width=10)

    result_label.pack(side = 'left')
    output_label.pack(side = 'left')


    # a function to calculate conversion and prompt its result in a dialog
    def convert_cm():
        # use .get() method to retrieve the data from an Entry widget
        cm = float(user_input_value.get()) # convert into float()
        result = round(cm / 2.54, 2)
        value.set(result) # set calculation result for StringVar object.

    # a button will trigger the calculating function
    button_convert = tkinter.Button(window, text = 'Convert', command = convert_cm)
    button_convert.pack(side = 'left')

    tkinter.mainloop()

main()
