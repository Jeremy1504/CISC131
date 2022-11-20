def passing_rate(filename):
    
    import random

    # generate random numbers and write file

    outfile = open(filename,'w')
    
    for i in range(200):
        line = str(random.randint(0, 100)) + '\n'
        outfile.write(line)
    
    outfile.close()
    
    # read file
    infile = open(filename, 'r')
   
    num_score = 0
    pass_count = 0
    
    for line in infile:
        if int(line.strip())>=60:
            pass_count += 1
        num_score += 1
        
    print('The passing rate is ', pass_count/num_score)

    infile.close()
    
passing_rate('Unit 09/more_exercise.txt')
