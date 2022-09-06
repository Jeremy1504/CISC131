# First we define the main function
def main():
    print('I want to call another function')
    message() # call another function
    print('Jump back to here')

# Next we define the message function
def message():
    print('The message() function is called!')
    print('The statements in this block are executed!')
    
# Call the main function.
main()

