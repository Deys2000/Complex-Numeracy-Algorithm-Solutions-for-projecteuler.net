def chain_length(number):
    count = 1
    while number > 1:
        if(number%2 == 0):
            number = number//2
            count += 1
        else:
            number = 3*number +1
            count += 1
    return count


max_chain = 0
value = 0
for x in range(1,1000000,1):
    chain = chain_length(x)
    #print(x,chain)
    if(chain>max_chain):
        max_chain = chain
        value = x
        print(x,chain)
print(str(value) + ":" + str(max_chain))


#the answer I get from this is
# 837799 gives a chain of 525
        
