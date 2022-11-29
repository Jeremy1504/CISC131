import tkinter
import tkinter.messagebox # import messagebox moudule

def main():
    window = tkinter.Tk()

    # display an info dialog box
    def print_message():
        tkinter.messagebox.showinfo('Response', 'Thank you for clicking!')

    # a button will trigger another function
    button = tkinter.Button(window, text = 'Click Me!', command = print_message)
    button.pack()

    tkinter.mainloop()

main()
