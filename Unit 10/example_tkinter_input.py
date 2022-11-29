import tkinter
import tkinter.messagebox # import messagebox moudule

def main():
    window = tkinter.Tk()

    # create label and user's input box
    user_input_label = tkinter.Label(window, text = 'Enter a length in centimeters: ')
    user_input_value = tkinter.Entry(window, width = 10)
    
    user_input_label.pack(side = 'left')
    user_input_value.pack(side = 'left')

    # a function to calculate conversion and prompt its result in a dialog
    def convert_cm():
        # use .get() method to retrieve the data from an Entry widget
        cm = float(user_input_value.get()) # convert into float()
        result = round(cm / 2.54, 2)  # convert cm to inches
        
        # display the results in a single concatenated string
        tkinter.messagebox.showinfo('Result', str(result)+ ' inch(es)')

    # a button will trigger the calculating function
    button_convert = tkinter.Button(window, text = 'Convert', command = convert_cm)
    button_convert.pack(side = 'left')

    tkinter.mainloop()

main()
