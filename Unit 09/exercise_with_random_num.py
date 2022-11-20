import random

def write_read_number(filename):
    with open(filename,'w') as fp:
    
        for i in range(10):
            line = str(random.randint(10,20)) + ' '
            fp.write(line)
    
    with open(filename, 'r') as fp:
        content = fp.read().split()
    
    length = len(content)
    sum_up = 0
    
    for item in content:
        sum_up += int(item.strip())

    print('Read {} items'.format(length))
    print('The average is ', sum_up/length)


write_read_number('Unit 09/number.txt')