def avg(*num):
    count = 0
    total = 0
    for i in num:
        total += i
        count += 1
    return total/count

print(avg(1, 3, 5, 7, 9))
print(avg(10, 20, 30))
print(avg(100, 100))
