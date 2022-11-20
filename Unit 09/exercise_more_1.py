import random

def write_read_text(filename):
    outfile = open(filename,'w')
    
    for i in range(100):
        line = str(random.randint(1,5)) + '\n'
        outfile.write(line)

    outfile.close()
    
    infile = open(filename, 'r')

    length = 0
    sum_up = 0
    
    for item in infile:
        sum_up += int(item.strip())
        length += 1
    print('Read {} items'.format(length))
    print('The average is ', sum_up/length)

    infile.close()

    # call count element function
    for i in range(1, 5):
        print('{} occurrs {} times'.format(i, count_element(filename, i)))

    
def count_element(filename, i):
    # require re-open file
    infile = open(filename, 'r')

    count = 0
    for item in infile:
        if (int(item.strip()) == i):
            count += 1

    infile.close()

    return count

    
write_read_text("Unit 09/more_exercise.txt")
