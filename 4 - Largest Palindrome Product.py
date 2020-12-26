

def is_it_divisible(value):
    for x in range(999,100,-1):
        if(value%x == 0):
            return x
    return -1


for x in range(999*999,100000,-1):
    chars = list(str(x))
    chars.reverse()
    reverse_value = int(''.join(chars))
    if(x == reverse_value and is_it_divisible(x) > 100) and x/is_it_divisible(x) <= 999:
            print(x)
            break
