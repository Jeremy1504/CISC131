degree = 20

print('celsius fahrenheit')
for celsius in range(0, degree+1):
    fahrenheit = 9/5*celsius+32
    print(f'{celsius:>5.2f} \t {fahrenheit:>5.2f}')
