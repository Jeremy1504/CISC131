# initialize flag variables
exam_flag = False
bad_weather_flag = False

# ask user's inputs
temperature = float(input('Please Enter the temperature: '))
precipitation_rate = float(input('Please Enter the precipitation chance: '))

# check conditionals
if temperature < 30 and precipitation_rate >= 50:
    bad_weather_flag = True

if precipitation_rate >=50:
    bad_weather_flag = True

# display what to do next
if not (exam_flag or bad_weather_flag):
    print('Go to party! :)')
else:
    print('Go to study. :(')
