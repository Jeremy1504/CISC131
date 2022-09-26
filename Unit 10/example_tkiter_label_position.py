import tkinter

def main():
    window = tkinter.Tk()

    # create a label widget
    label_1 = tkinter.Label(window, text = 'Welcome CISC131')
    label_2 = tkinter.Label(window, text = 'The First GUI program.')
    label_3 = tkinter.Label(window, text = 'Hello World')

    # call the widget's pack method
    label_1.pack(side = 'top')
    label_2.pack(side = 'left')
    label_3.pack(side = 'right')

    tkinter.mainloop()

main()
