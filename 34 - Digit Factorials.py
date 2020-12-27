#brrrrrute force, but i think that was the only way for this anyway...
def factorial(num):
    ans = 1
    for x in range(num,1,-1):
        ans *= x
    return ans

sum = 0
running_sum = 0
string_x = ''
for x in range(3, 1000000):
    string_x = str(x)
    for i in range(0,len(string_x)):
        sum += factorial(int(string_x[i]))
    if(sum == x):
        running_sum += x
        print(x, running_sum)
    sum = 0
print(running_sum)

        
