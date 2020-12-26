
def is_prime(num):
    for x in range(2,num//2+1):
        if(num%x ==0):
            return False
    return True
storeA = 0
storeB = 0
consecutive = 0
for b in range(3,1001,2):
    if(is_prime(b) == True):
        for a in range(1,1000,2):
            if(is_prime(a)):
                n = 0
                while( is_prime(n**2 + a*n + b) == True):
                    print(a,b, consecutive)
                    if(n>consecutive):
                        consecutive = n
                        storeA = a
                        storeB = b
                    n += 1

print(storeA, storeB, consecutive, storeA*storeB)
                    
