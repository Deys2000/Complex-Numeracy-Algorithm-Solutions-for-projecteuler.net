# brute force, program can still be maximized
import math
max_count = 0
max_p = 0
for p in range(3, 1000):
    count = 0
    for a in range(1, p-2):
        for b in range(1, p-2-a):
            c = math.sqrt(a**2+b**2)
            if( c == (p - a - b)):
                count += 1
                #print(a,b,c,p)
                if( max_count < count):
                    max_count = count
                    max_p = p
                    
print(max_p,max_count)
            
