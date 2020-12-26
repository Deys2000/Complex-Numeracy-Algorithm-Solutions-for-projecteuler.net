a = 1
b = 100
sum = 0
for x in range(a,b+1):
    sum += x**2
difference = (b//2+(b*((b+a)//2)))**2 - sum #im not sure if this line is right
print(difference)
