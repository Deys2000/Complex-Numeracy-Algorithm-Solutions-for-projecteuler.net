# i messed up here, i thought it just meant the reverse, but i need the lexicograph switcher first to do this...

def reverse_str(str):
    return str[::-1]

import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

count = 1
for x in range(3, 1000000,2):
    string_x = str(x)
    if(is_prime(x) == True and is_prime(int(reverse_str(string_x)))==True):
        print(count,x)
        count+=1
print(count)
