def sum_of_divisors(num):
    sum=0
    decreased_bound = int(num**.5)+1
    for x in range(2,decreased_bound,1):
        if(num%x == 0):
            sum += x
            if(num/x != x):
                sum += num/x
    return sum + 1

def exist_in_array(list,num):
    for x in range(0,len(list)):
        if(num == list[x]):
            return True
    return False

running_sum =0
amicables = [1]

for x in range(2,10000):
    possible_amicable = sum_of_divisors(x)
    if(possible_amicable<10000 and possible_amicable!= x):         
        if(x == sum_of_divisors(possible_amicable)):
            print(x, sum_of_divisors(x), sum_of_divisors(possible_amicable))   
            running_sum += x
            print(running_sum)
print(running_sum)
