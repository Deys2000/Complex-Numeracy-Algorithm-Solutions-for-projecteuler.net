#program takes too long...
primelist = [2,3,5,7,11]
def number_is_prime(num):
    for x in range(0,len(primelist)):
        if(num%primelist[x] == 0):
            return False
    primelist.append(num)
    return True


sum = 0
for x in range(3,2000000,2):
    if(number_is_prime(x) == True):
        sum+=x
print(sum)
