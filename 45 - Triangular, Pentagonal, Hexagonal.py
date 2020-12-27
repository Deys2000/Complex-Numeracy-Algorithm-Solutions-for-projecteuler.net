array_tri = []
array_pent = []
array_hex =[]

limit = 100000

for x in range(1,limit,1):
    array_tri.append((x*(x+1))/2)
    array_pent.append((x*((3*x)-1))/2)
    array_hex.append(x*((2*x)-1))
#print(array_pent)

for y in range(0,limit-1,1):
    if (array_hex[y] in array_pent) and (array_hex[y] in array_tri):
        print(array_hex[y], y)


#found it, but not proud of solution, i just used brute force
# 1 and 1
# 40755 and H143
# 1533776805 and H27692
