
def read_fruits(filename):

    with open(filename, 'r') as fp:
        content = fp.read().split('\n')
    print(content)

    count_apple = 0
    count_banana = 0
    count_peach = 0

    for item in content:
        if item == 'apple':
            count_apple += 1
        elif item == 'banana':
            count_banana += 1
        elif item == 'peach':
            count_peach += 1
    
    print(f'Number of apple: {count_apple}')
    print(f'Number of banana: {count_banana}')
    print(f'Number of peach: {count_peach}')

read_fruits('fruits.txt')