
a = 1
b = 1
sum = 0
c = 2
while c <= 4000000:
    if(c%2 == 0):
        print(c)
        sum = sum + c
    a = b
    b = c
    c = a+b

print(sum)
