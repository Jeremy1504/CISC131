import tkinter
import tkinter.messagebox # import messagebox moudule

def main():
    window = tkinter.Tk()

    # create two frames to group widgets
    top_frame = tkinter.Frame(window)
    bottom_frame = tkinter.Frame(window)

    # create label and user's input box
    user_input_label = tkinter.Label(top_frame, text = 'Enter a length in centimeters: ')
    user_input_value = tkinter.Entry(top_frame, width = 10)
    
    user_input_label.pack(side = 'left')
    user_input_value.pack(side = 'left')

    # a function to calculate conversion and prompt its result in a dialog
    def convert_cm():
        # use .get() method to retrieve the data from an Entry widget
        cm = float(user_input_value.get()) # convert into float()
        inch = round(cm / 2.54, 2)
        
        # display the results in a single concatenated string
        tkinter.messagebox.showinfo('Result', str(inch)+ ' inch(es)')

    # a button will trigger the calculating function
    button_convert = tkinter.Button(bottom_frame, text = 'Convert', command = convert_cm)
    button_quit = tkinter.Button(bottom_frame, text = 'Quit', command = window.destroy)
    
    # pack button
    button_convert.pack(side = 'left')
    button_quit.pack(side = 'left')
    # pack frame
    top_frame.pack()
    bottom_frame.pack()

    tkinter.mainloop()

main()
