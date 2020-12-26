import math

a = 0
b = 0
is_ans = False

while True:
    b+=1
    a=0
    while True:
        a += 1
        c = math.sqrt(a**2 + b**2)
        if(a+b+c > 1000):
            break
        if(a+b+c == 1000):
            is_ans = True
            break
    if(is_ans):
        break
print(a,b,c,a*b*c)
