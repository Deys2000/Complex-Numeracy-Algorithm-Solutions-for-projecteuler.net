array_tri = []
array_pent = []
array_hex =[]

limit = 300

for x in range(1,limit,1):
    array_tri.append((x*(x+1))/2)
    array_pent.append((x*((3*x)-1))/2)
    array_pent.append(x*((2*x)-1))
#print(array_pent)

for y in range(0,limit-1,1):
    if (array_tri[y] in array_pent) and (array_tri[y] in array_hex):
        print(array_tri[y], y)
