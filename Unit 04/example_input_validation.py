score = int(input('Enter a test score: '))
while score < 0 or score > 100:
	print('Error: Score should be in range from 0 to 100')
	score = int(input('Enter a valid score: '))


