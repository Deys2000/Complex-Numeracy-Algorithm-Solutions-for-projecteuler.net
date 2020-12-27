a = 1
b = 1
c = 0
index = 2

digit = 0
while digit != 1000:
    c = a + b
    digit = len(str(c))
    index += 1
    a = b
    b = c
print(index, c)
 
    
    
