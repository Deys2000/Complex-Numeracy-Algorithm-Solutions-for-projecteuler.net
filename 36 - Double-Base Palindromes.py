#brute force again
def dec_to_bin(x):
    return int(bin(x)[2:])
def reverse_str(str):
    return str[::-1]

sum = 0
for dec in range(0,1000000):
    string_dec = str(dec)
    string_bin = str(dec_to_bin(dec))
    if(string_dec == reverse_str(string_dec) and string_bin == reverse_str(string_bin)):
        sum += dec
        print(dec,sum)
print('total',sum)
