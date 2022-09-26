import tkinter
import tkinter.messagebox # import messagebox moudule

def main():
    window = tkinter.Tk()

    # display an info dialog box
    def print_message():
        tkinter.messagebox.showinfo('Response', 'Thank you for clicking!')

    # Thank you button
    button_click = tkinter.Button(window, text = 'Thank you!', command = print_message)

    # Quit you button
    button_quit = tkinter.Button(window, text = 'Quit', command = window.destroy)

    button_click.pack()
    button_quit.pack()

    tkinter.mainloop()

main()
