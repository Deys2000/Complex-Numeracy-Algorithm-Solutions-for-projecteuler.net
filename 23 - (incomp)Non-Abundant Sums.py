import math
def list_of_proper_factors(number):
    all_proper_factors = []
    all_proper_factors.append(1)
    for x in range(2, int(math.sqrt(number)) + 1,1):
        if( number%x == 0):
            all_proper_factors.append(x)
            all_proper_factors.append(number//x)
    if( int(math.sqrt(number)) == math.sqrt(number)):
        all_proper_factors.pop(len(all_proper_factors)-1)
    return all_proper_factors

print(list_of_proper_factors(24))



#this method works!!
def sum_of_divisors(num):
    sum=0
    decreased_bound = int(num**.5)+1
    for x in range(2,decreased_bound,1):
        if(num%x == 0):
            sum += x
            if(num/x != x):
                sum += num/x
    return sum + 1

print(sum_of_divisors(24))

##
##array_of_abundants = []
###finding all abundant numbers
##for x in range(12, 28123):
##    if(x < sum_of_divisors(x)):
##        print(x)
##        array_of_abundants.append(x)
###make array with all addition possibilities
##array_of_combinations = []
##for x in range(0,len(array_of_abundants)):
##    for y in range(0,len(array_of_abundants)):
##        new = array_of_abundants[x] + array_of_abundants[y]
##        print(new)
##        for z in range(0,len(array_of_combinations)):
##            if(new == array_of_combinations[z]):
##               break
##        array_of_combinations.append(new)
###make a max sum and subtract all values in array
##sum = 0
##for x in range(12,28123-12):
##    sum += x
##    print(sum)
##for x in range(0,len(array_of_combinations)):
##    sum -= array_of_combinations[x]
##    print(sum)
##
##print(sum)
