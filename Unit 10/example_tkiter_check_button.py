import tkinter
import tkinter.messagebox

def main():
    window = tkinter.Tk()

    # create two frames
    top_frame = tkinter.Frame(window)
    bottom_frame = tkinter.Frame(window)
    
    # create three variables to store values for checked options
    cb_var_1 = tkinter.IntVar()
    cb_var_2 = tkinter.IntVar()
    cb_var_3 = tkinter.IntVar()
    
    # initilize their values with 0: uncheked
    cb_var_1.set(0)
    cb_var_2.set(0)
    cb_var_3.set(0)

    # create three Checkbutton widgets
    # different value when selected
    cb_1 = tkinter.Checkbutton(top_frame, text = 'Option 1', variable = cb_var_1)
    cb_2 = tkinter.Checkbutton(top_frame, text = 'Option 2', variable = cb_var_2)
    cb_3 = tkinter.Checkbutton(top_frame, text = 'Option 3', variable = cb_var_3)

    cb_1.pack()
    cb_2.pack()
    cb_3.pack()

    # show a dialog message which radio button selected
    def show_choice():
        # create a string
        message = 'You selected: '
        # check which Checkbuttons are selected and build the message accordingly
        if cb_var_1.get() == 1:
            # string concatenation
            message = message + '1,'
        if cb_var_2.get() == 1:
            message = message + '2,'
        if cb_var_3.get() == 1:
            message = message + '3,'
        # display the selection messages        
        tkinter.messagebox.showinfo('Selection', message)

    # create an OK button to trigger the show_choice() function
    button_ok = tkinter.Button(bottom_frame, text = 'OK', command = show_choice)
    button_ok.pack(side = 'left')

    top_frame.pack()
    bottom_frame.pack()

    tkinter.mainloop()

main()
