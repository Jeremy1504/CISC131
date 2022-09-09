def quotientAndRemainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    # Returns the tuple of the quotient and remainder
    return (quotient, remainder)

(myQuotient, myRemainder) = quotientAndRemainder(10, 3)

print("Quotient:", myQuotient)
print("Remainder:", myRemainder)

