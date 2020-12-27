# theres another way to find factors and such, i need to understand the python syntax and math formulas
##def num_of_factors(num):
##    leftover = 0
##    exponents =()
##    x = 2
##    while True:
##        if(num%x == 0):
##            leftover = num/x
##            if(
##            exponents.append(x)
##            num = leftover
##     
##term_count = 0
##triangle_value = 0
##while True:
##    term_count += 1
##    triangle_value += term_count
##    nof = num_of_factors(triangle_value)
##    print(term_count,triangle_value,nof)
##    if( nof > 500):
##        print(term_count, triangle_value)
##        break
    
#i am thinking that i have a formula that
#takes a number and finds the number of factors it has
import math
def num_of_factors(number):
    amount = 2
    for x in range(2, int(math.sqrt(number)) + 1,1):
        if( number%x == 0):
            amount = amount + 2
    if( int(math.sqrt(number)) == math.sqrt(number)):
        return amount - 1
    return amount
##answer = num_of_factors(28)
##print(answer)
answer = 0
runningValue = 0
for x in range(1, 20000, 1):
    runningValue = runningValue + x
    answer = num_of_factors(runningValue)
    print(str(x) + " : " + str(runningValue) + " : " + str(answer))
    if(answer>500):
        break

# i got at the 12375th triangle number
# the value for it is 76576500
# and the amount of factors is 576

