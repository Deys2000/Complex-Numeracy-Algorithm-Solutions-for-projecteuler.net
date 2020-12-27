import math
def is_prime(num):
    if(num%2 == 0 and num>2):
        return False
    for i in range(3,int(math.sqrt(num))+1, 2):
        if(num%i == 0):
            return False
    return True

#check if a number is prime taking off each digit from the left like so: 3796,796,96,6
def left_check(num):
    num_string = str(num)
    for x in range(len(num_string)-1,0,-1):
        if(is_prime(num%10**x )==False):
            return False
    return True

def right_check(num):
    num_string = str(num)
    for x in range(1,len(num_string)):
        if(is_prime(num//10**x) == False):
            return False
    return True
def no_one(num):
    num_string = str(num)
    if(num_string[0] == '1' or num_string[len(num_string)-1] == '1'):
            return False
    return True


sum = 0
for number in range(11, 1000000):
    if( is_prime(number) and right_check(number) and left_check(number) and no_one(number)):
        print(number)
        sum += number
print('sum: ',sum)

