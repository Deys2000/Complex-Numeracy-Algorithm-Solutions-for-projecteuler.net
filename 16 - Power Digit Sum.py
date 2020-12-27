x = 2**1000
string_x = str(x)
sum = 0
for x in range(0,len(string_x)):
    sum += int(string_x[x])
print(sum)
