array = [1]
for b in range(2,101):
    for ex in range(2,101):
        current = b**ex
        matches = False
        for i in range(0,len(array)):
            if(current == array[i]):
                matches = True
                break
        if(matches==False):
            array.append(current)

print(len(array)-1)
