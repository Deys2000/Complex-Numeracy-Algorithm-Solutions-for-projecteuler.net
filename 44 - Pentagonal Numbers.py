array = []

amount = 10000

for x in range(1,amount,1):
    array.append((((3*x)-1)*x)/2)
print(array)

smallestD = 9999999

for x in range(0,amount-2,1):
    for y in range(x+1,amount-1,1):
        
        if (array[y] + array[x]) in array and(array[y] - array[x]) in array:
            print("HERE")
            print(array[y]-array[x], array[x], array[y], array[x] + array[y])
            if(smallestD > abs(array[y] -array[x])):
                smallestD = (array[y] -array[x])
       
print(smallestD)
