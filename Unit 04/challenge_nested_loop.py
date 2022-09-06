row = 5
column = 5

# i loop from [1, row]
for i in range(1, row+1):
    # j loop from [1, column]
    for j in range(1, column+1):
        print(f'{i}*{j}={i*j}\t', end = '') # concatenate w/o changing to the next line
    print() # change w/ next line