row = 5
column = 5

for i in range(1, row+1):
    print(f'Outer Loop: {i} th iteration')
    for j in range(1, column+1):
        print(f'    {j} th iteration: ',  end = ' ')
        print(f'{i}*{j}={i*j}\t', end = '')
    print()


