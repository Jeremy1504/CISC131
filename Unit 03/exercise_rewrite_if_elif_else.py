x = 10 
if x > 9: 
    print('Yays!') 
else: 
    if x > 7: 
        print('Wait')      
    else:
        if x > 3:
            print('Yep') 
        else:
            print('Jump!')

# rewrite
x = 10
if x > 9: 
    print('Yays!')
elif x > 7: 
    print('Wait')
elif x > 3:
    print('Yep')
else:
    print("Jump!")
