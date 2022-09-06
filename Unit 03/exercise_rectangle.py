first_length = float(input('Please the length of first rectangle: '))
first_width = float(input('Please the width of first rectangle: '))
second_length = float(input('Please the length of second rectangle: '))
second_width = float(input('Please the width of second rectangle: '))

first_area = first_length * first_width
second_area = second_length * second_width

if first_area > second_area:
	print('The area of the first rectangle is greater.')
if first_area < second_area:
	print('The area of the second rectangle is greater.')
else:
	print('The areas of two rectangles are the same.')

