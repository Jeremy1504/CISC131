rows = 5
# outer loop
for i in range(rows, 0, -1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end="")
    print("")
