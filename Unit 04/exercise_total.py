# arithmetic sequence
# 1+2+3+..+9
total = 0
for i in range (1, 10):
	total = total + i
print(total)

#################################
# arithmetic sequence
# 1+2+3+..+99+100
total = 0
for i in range (1, 101):
	total = total + i
print(total)


#################################
# arithmetic sequence
# 1+3+5+..+97+99
total = 0
for i in range (1, 100, 2):
	total = total + i
print(total)


#################################
# arithmetic sequence
# 2+4+6+...+98+100
total = 0
for i in range (2, 101, 2):
	total = total + i
print(total)

#################################
# sum of square numbers
# 1^2 + 2^2 + ... + 99^2 + 100^2

total = 0
for i in range (1, 101, 1):
	total = total + i**2
print(total)

#################################
# sum of square numbers
# 1^2 + 3^2 + ... + 97^2 + 99^2

total = 0
for i in range (1, 101, 1):
	total = total + i**2
print(total)

#################################
# sequence
# 1^1 + 2^2 + ... + 9^9 + 10^10

total = 0
for i in range (1, 11, 1):
	total = total + i**i
print(total)