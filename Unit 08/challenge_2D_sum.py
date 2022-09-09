A = [[2, -4, -6, 8],
    [1, 3, 5, 7],
    [10, 20, 30, 40]]

# sum all numbers by row
for row in A:
    total = 0
    for item in row:
        total += item
    print('Row Total: ', total)

