def sumCount(n):
    if n <= 1:
        return n
    else:
        return n + sumCount(n - 1)

print(sumCount(100))
