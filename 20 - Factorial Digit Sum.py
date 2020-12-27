def calculate_factorial(num):
    value = 1
    for x in range(num,0,-1):
        value*=x
    return value

string_value = str(calculate_factorial(100))
digit_value = 0
running_count = 0
for x in range(0,len(string_value)):
    digit_value = int(string_value[x])
    running_count += digit_value
print(running_count)
