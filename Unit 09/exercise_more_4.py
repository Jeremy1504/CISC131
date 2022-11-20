
def read_text(filename):
    
    infile = open(filename, 'r')
   
    count = 0
    for line in infile:
        print('{}; {}'.format(count+1, line.strip()))
        count += 1

    infile.close()

read_text('Unit 09/demo86.txt')