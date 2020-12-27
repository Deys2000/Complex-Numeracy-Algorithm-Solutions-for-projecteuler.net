#each corner allows two choices, this is some sort of exponential problem
# 1by1 = 2
# 2by2 = 6
# 3by3 = 20
# 4by4 = 70

num_of_sides = 20
results = []
for x in range(0,num_of_sides, 1):
    results.append(1)
print(results)

for x in range(0,num_of_sides-1,1):
    results[0] = results[1]*2
    for y in range(1,len(results)-1):
        results[y] = results[y+1] + results[y-1]
    results.pop(len(results)-1)
    print(results)
    
#  this is the answer i got for 20 sides: 35345263800
