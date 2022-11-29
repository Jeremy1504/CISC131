# tkinter works on Windows OS by default
# Mac OS user might need to install this package using `pip3 install tk`
# Linux OS user needs to install using `apt-get install python-tk`

import tkinter

# wrap in a main() function
def main():
    # creat a Tk window
    window = tkinter.Tk()
    # run the main loop for tkinter object
    tkinter.mainloop()

main()
