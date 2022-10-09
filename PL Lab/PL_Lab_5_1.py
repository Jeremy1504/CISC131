def taxReport(sales):
    country_tax = 0.04 * sales
    state_tax = 0.02 * sales
    
    total_sales = country_tax + state_tax
    
    print('The amount of county sales tax ', country_tax)
    print('The amount of state sales tax ',  state_tax)
    print('The total sales tax (county plus state) ', total_sales)

taxReport(60000)
taxReport(70000)
taxReport(65000)

def drawPattern(num, symbol):

    # range for rows
    for i in range(1, num+1):
        # print for each row
        for j in range(1, i+1):
            print(symbol, end='')

        print()

# test case
drawPattern(3, '*')
drawPattern(5, '#')
drawPattern(6, '-')