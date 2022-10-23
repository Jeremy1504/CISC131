import tkinter
import tkinter.messagebox # import messagebox moudule

def main():
    window = tkinter.Tk()

    # create three frames to group widgets
    top_frame = tkinter.Frame(window)
    mid_frame = tkinter.Frame(window)
    bottom_frame = tkinter.Frame(window)

    # create label and user's input box
    user_input_label = tkinter.Label(top_frame, text = 'Enter a length in centimeters: ')
    user_input_value = tkinter.Entry(top_frame, width = 10)
    
    user_input_label.pack(side = 'left')
    user_input_value.pack(side = 'left')

    # Create the widgets for the middle frame
    result_label = tkinter.Label(mid_frame, text = 'Converted to inches: ')

    # create a StringVar object and store a string of blank char.
    value = tkinter.StringVar()
    # Create a label and associate it with the StringVar object.
    # its value will be stored in StringVar object will automatically be displayed in the label
    cm_value_label = tkinter.Label(mid_frame, textvariable = value)

    # pack middle frame's widgets
    result_label.pack(side = 'left')
    cm_value_label.pack(side = 'left')


    # a function to calculate conversion and prompt its result in a dialog
    def convert_cm():
        # use .get() method to retrieve the data from an Entry widget
        cm = float(user_input_value.get()) # convert into float()
        inch = round(cm / 2.54, 2)
        value.set(inch) # set calculation result for StringVar object.

    # a button will trigger the calculating function
    button_convert = tkinter.Button(bottom_frame, text = 'Convert', command = convert_cm)
    button_quit = tkinter.Button(bottom_frame, text = 'Quit', command = window.destroy)
    
    # pack button
    button_convert.pack(side = 'left')
    button_quit.pack(side = 'left')

    # pack frame
    top_frame.pack()
    mid_frame.pack()
    bottom_frame.pack()

    tkinter.mainloop()

main()
