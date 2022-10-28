def simple_interest(amount, year, rate):
    try:
        if rate > 100:
            raise ValueError(rate) # raise ValueError
        interest = (amount * year * rate) / 100
        print('The Simple Interest is', interest)
        return interest
    except ValueError: # catch the raised ValueError
        print('interest rate is out of range', rate)

print('Case 1')
simple_interest(800, 6, 8)

print('Case 2')
simple_interest(800, 6, 800)
