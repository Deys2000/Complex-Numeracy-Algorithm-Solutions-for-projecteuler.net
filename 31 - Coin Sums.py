#brute force, you can make it better by putting in skips and better starter for the loops instead of 0
a = 1
b = 2
c = 5
d = 10
e = 20
f = 50
g = 100
h = 200
count = 0

for i in range(0,200//h +1):
    for j in range(0,200//g +1):
        for k in range(0,200//f +1):
            for l in range(0,200//e +1):
                for m in range(0,200//d +1):
                    for n in range(0,200//c +1):
                        for o in range(0,200//b +1):
                            for p in range(0,200//a +1):
                                sum = i*h + j*g + k*f + l*e + m*d + n*c + o*b + p*a
                                if(sum > 200):
                                    break
                                if(sum == 200):
                                    count +=1
print(count)    
