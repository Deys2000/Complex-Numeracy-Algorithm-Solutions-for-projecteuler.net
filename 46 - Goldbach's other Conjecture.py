#so basically, i go up a list of composites
#and subtract increasing doubles of squares until i am negative
#then move on to the next composite
#the answer will be found when the subtraction result is false for composite

def isComposite (number):
    if(number%2 == 0 and number!=2):
        return True
    for x in range(3, number//2, 2):
        if( number % x == 0):
            return True
    return False
def subtractSquares_checkAnomaly(number):
    difference = 0
    squareCount = 1
    while difference >=0:
        difference = number -(squareCount*squareCount*2)
        squareCount = squareCount + 1
        if (difference > 1 and isComposite(difference) == False):
           return False
    return True
    
for x in range( 9,10000,2):
    if( isComposite(x) == True):
        if( subtractSquares_checkAnomaly(x) == True):
            print(x)
        


