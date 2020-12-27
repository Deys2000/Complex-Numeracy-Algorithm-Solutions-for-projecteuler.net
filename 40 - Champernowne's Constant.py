running_multiplier = 1
cnt = 0
for d in range(1,1000001):
    string = str(d)
    for i in range(0,len(string)):
        current = int(string[i])
        cnt += 1
        if(cnt == 1 or cnt == 10 or cnt == 100 or cnt == 1000 or cnt == 10000 or cnt == 100000 or cnt == 1000000):
            running_multiplier *= current
print(running_multiplier)
    
