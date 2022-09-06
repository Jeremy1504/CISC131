import random

count_even = 0
count_odd = 0

for i in range(0, 100):
    num = random.randint(1, 100)
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print('Even: ', count_even)
print('Odd: ', count_odd)
