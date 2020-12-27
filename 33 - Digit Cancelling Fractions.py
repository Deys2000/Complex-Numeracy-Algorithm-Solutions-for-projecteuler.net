#brute force again...
def reduce_fraction(num,den):
    new_num = 0.0
    new_den = 0.0
    if(num < den):
        limit = den
    else:
        limit = num
    for x in range(limit//2 +2,2,-1):
        new_num = num / x
        new_den = den / x
        if(new_num%1 == 0.0 and new_den%1 == 0.0):
            string = str(new_num)+'/'+str(new_den)
            return(string)

print(reduce_fraction(10,20))

frac = 0.0
running_product_num = 1
running_product_den = 1
for n1 in range(1,10):
    for n2 in range(1,10):
        for d1 in range(n1,10):
            for d2 in range(1
                            ,10):
                num = n1*10 + n2
                den = d1*10 + d2
                frac = num/den
                if(num!=den and ((frac== n1/d1 and n2==d2) or (frac ==n1/d2 and n2==d1) or (frac == n2/d1 and n1==d2) or (frac == n2/d2 and n1==d1))):
                    print(num,den)
                    running_product_num *= num
                    running_product_den *= den
print(running_product_num,running_product_den)
print(reduce_fraction(running_product_num,running_product_den))
