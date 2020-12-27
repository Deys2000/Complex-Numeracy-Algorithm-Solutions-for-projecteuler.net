# i just assume its not possible after 1 million
running_sum = 0
string_x = ''
array = []
for x in range(31, 1000000):
    sum = 0
    string_x = str(x)
    for i in range(0,len(string_x)):
        sum += int(string_x[i])**5
    if(sum == x ):
        print(sum)
        running_sum += sum

print('answer',running_sum)
