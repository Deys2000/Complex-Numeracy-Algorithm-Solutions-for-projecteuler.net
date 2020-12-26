primelist = [2]
def number_is_prime(num):
    for x in range(0,len(primelist)):
        if(num%primelist[x] == 0):
            return False
    primelist.append(num)
    return True

count = 0
number = 2

while True:
    if(number_is_prime(number) == True):
        #print(number)
        count+= 1
        if(count == 100001):
            break
    number += 1
print(number-1)
