def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
                

        return True
    else:
        return False


for i in range(1, 101):
    if is_prime(i):
        print(i, end = ' ')
