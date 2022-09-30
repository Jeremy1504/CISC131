# 1, 6, 11, 16, 21, 26, ... 91, 96
for i in range(1, 100, 5):
    print(i, end = ' ')
print()

# 2, 4, 8, 16, ... 2048
for i in range(1, 12):
    j = 2 ** i
    print(j, end = ' ')

print()

# 1, 11, 111, 1111, ... 111111
j = 0
for i in range(6):
    j = j * 10 + 1
    print(j, end = ' ')