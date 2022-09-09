A = [[2, -4, -6, 8],
    [1, 3, 5, 7],
    [10, 20, 30, 40]]

print(A[0][0])
print(A[0][1])
print(A[1][0])
try:
    print(A[2][4])
except IndexError:
    print('Index Error')
print(A[-1][-1])
