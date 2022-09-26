import tkinter

def main():
    window = tkinter.Tk()

    # create a label widget
    label = tkinter.Label(window, text = 'Hello World')

    # call the widget's pack method
    label.pack()
    # run as an infinite loop until close the main window
    tkinter.mainloop()

main()
