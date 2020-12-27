array = []
x =1
quad = 0
layer = 1
while x < 1001*1001:
    x += layer+1
    quad += 1
    array.append(x)
    if(quad == 4):
        layer += 2
        quad = 0
sum = 1
for x in range(0,len(array)):
    sum += array[x]
print(sum)
    
