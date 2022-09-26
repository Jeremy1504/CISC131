import tkinter
import tkinter.messagebox

def main():
    window = tkinter.Tk()

    # create two frames
    top_frame = tkinter.Frame(window)
    bottom_frame = tkinter.Frame(window)
    
    # a variable to store unique integer when radio button selected
    radio_var = tkinter.IntVar()
    # set default value
    radio_var.set(1)

    # create three Radiobutton widgets
    # different value when selected
    radio_button_1 = tkinter.Radiobutton(top_frame, text = 'Option 1', variable = radio_var, value = 1)
    radio_button_2 = tkinter.Radiobutton(top_frame, text = 'Option 2', variable = radio_var, value = 2)
    radio_button_3 = tkinter.Radiobutton(top_frame, text = 'Option 3', variable = radio_var, value = 3)

    radio_button_1.pack()
    radio_button_2.pack()
    radio_button_3.pack()

    # show a dialog message which radio button selected
    def show_choice():
        tkinter.messagebox.showinfo('Selection', 'You selected option ' + str(radio_var.get()))

    # create an OK button to trigger the show_choice() function
    button_ok = tkinter.Button(bottom_frame, text = 'OK', command = show_choice)
    button_ok.pack(side = 'left')

    top_frame.pack()
    bottom_frame.pack()

    tkinter.mainloop()

main()
