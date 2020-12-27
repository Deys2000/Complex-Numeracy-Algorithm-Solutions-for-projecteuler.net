def swap(array,x,y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
    

a = 0
b = 1
c = 2
d = 3
e = 4
num = [a,b,c,d,e]
print(num)
for h in range(0,2):
    swap(num,len(num)-5,h)
    for i in range(1,5):
        swap(num,len(num)-4,i)
        for j in range(0,2):
            swap(num,len(num)-2,len(num)-1)
            print(num)

