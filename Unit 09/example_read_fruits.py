# create a function
def read_fruits(filename):
    # open file and read the content
    with open(filename, 'r') as fp:
        # split the file by a white spaces
        # store the splited data in a list
        content = fp.read().split('\n')
    # preview the read content
    print(content)

    # initialize three couter variables 
    count_apple = 0
    count_banana = 0
    count_peach = 0

    # use a for loop to iterate over the list
    for item in content:
        # if we found the apple
        if item == 'apple':
            # counter increases by 1
            count_apple += 1
        elif item == 'banana':
            count_banana += 1
        elif item == 'peach':
            count_peach += 1
    
    # print the final results
    print(f'Number of apple: {count_apple}')
    print(f'Number of banana: {count_banana}')
    print(f'Number of peach: {count_peach}')

# call the function and pass the filename as the input argument
read_fruits('Unit 09/fruits.txt')