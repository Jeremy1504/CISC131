import tkinter

def main():
    window = tkinter.Tk()
    # create two frames
    top_frame = tkinter.Frame(window)
    bottom_frame = tkinter.Frame(window)

    # create three labels
    # assign label 1 to top frame
    label_1 = tkinter.Label(top_frame, text = 'Top Frame Label 1')
    # assign label 2 and label 3 to bottom frame
    label_2 = tkinter.Label(bottom_frame, text = 'Bottom Frame Label 2')
    label_3 = tkinter.Label(bottom_frame, text = 'Bottom Frame Label 3')

    # all labels set left-align
    label_1.pack(side = 'left')
    label_2.pack(side = 'left')
    label_3.pack(side = 'left')

    # top frame align on the top
    top_frame.pack(side = 'top')
    # bottom frame align in the bottom
    bottom_frame.pack(side = 'bottom')

    tkinter.mainloop()

main()
