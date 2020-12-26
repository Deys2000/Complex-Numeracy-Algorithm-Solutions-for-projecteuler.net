# put the number in a variable
# go up all nums until 1/3 of the number to see if each divisible by mod
# if it is divisible, then check the other number for primity
# get square root of variable
# check odd descendingly for mod by number
# if it is divisible, check for prime
import math
def isPrime(number):
    if(number%2 == 0 ):
        return False
    loops = int(math.sqrt(number) + .5) +1
    for x in range(3,loops,2):
        if( number%x == 0):
            return False
    return True
def biggestPrime(number):
    square_root = int(math.sqrt(number))+1
    for x in range(2, square_root ,1):
        if( number%x == 0 and isPrime(number/x)):
            return int(number/x)
    for y in range(square_root, 2, -1):
        if ( number%y ==0 and isPrime(y)):
            return y
        
    

print(biggestPrime(600851475143))

# i got 6857, check with other nums before entering




##
##primeList = [2,3,5]
##isPrime = True
##
##for x in range(6,600851475067):
##    for i in range(0,len(primeList)):
##        isPrime = True
##        y = int(math.sqrt(x))
##        if(primeList[i] <= math.sqrt(x) and x%primeList[i] == 0):
##            isPrime = False
##            break   
##    if(isPrime == True):
##        primeList.append(x)
##        print(x)
