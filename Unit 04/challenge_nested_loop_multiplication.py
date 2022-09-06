n = 9

for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        if i>=j:
            print('{}*{}={}\t'.format(i, j, i*j), end = '')
    print()
