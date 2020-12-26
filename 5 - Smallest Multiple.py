
def find_gcf(i,j): #i must be greater than j
    while True:
        r = i//j
        gcf = i -(r*j)
        if(gcf == 0):
            return j
        
        i = j
        j = gcf


a = 2
b = 20
lcd = 1
for x in range(a,b):
    divisor = find_gcf(lcd,x)
    lcd = lcd * x
    lcd = lcd // divisor
print(lcd)
    
    
        
    
