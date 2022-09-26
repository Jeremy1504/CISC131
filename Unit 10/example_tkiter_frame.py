import tkinter

def main():
    window = tkinter.Tk()
    top_frame = tkinter.Frame(window)
    bottom_frame = tkinter.Frame(window)

    label_1 = tkinter.Label(top_frame, text = 'CISC')
    label_2 = tkinter.Label(top_frame, text = '131')
    label_3 = tkinter.Label(top_frame, text = 'Python')
    label_1.pack(side= 'top')
    label_2.pack(side= 'top')
    label_3.pack(side= 'top')


    label_3 = tkinter.Label(bottom_frame, text = 'Chapter')
    label_4 = tkinter.Label(bottom_frame, text = 'GUI')



    label_3.pack(side= 'right')
    label_4.pack(side= 'right')

    top_frame.pack()
    bottom_frame.pack()

    tkinter.mainloop()

main()
