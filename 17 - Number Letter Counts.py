#code works, what i got is 21111


def unit_amount(num):
    int = 0
    if( num ==0 ):
        int = 0
    elif(num == '1' or num == '2' or num == '6' ):
        int = 3
    elif(num == '4' or num == '5' or num == '9' ):
        int = 4
    elif(num == '3' or num == '7' or num == '8' ):
        int = 5
    return int
def tens_amount(num):
    int = 0
    if(num == '4' or num == '5' or num =='6' or num =='9'):
        int = 5
    elif(num == '2' or num == '3' or num == '8'):
        int = 6
    elif(num == '7'):
        int =  7
    return int
def teen_amount(num):
    int = 0
    if(num == '11' or num == '12'):
        int = 6
    elif(num == '13' or num =='14' or num == '18' or num == '19'):
        int = 8
    elif(num == '15' or num =='16'):
        int = 7
    else:
        int = 9
    return int


sum = 0   
for x in range(1,1001,1):
    string_x = str(x)
    if(len(string_x) == 1):
        sum += unit_amount(string_x)        
    elif(len(string_x) == 2):
        if(int(string_x[0]) == 1):
            sum += teen_amount(string_x)
        else:
            sum += unit_amount(string_x[1]) + tens_amount(string_x[0])
    elif(len(string_x) == 3):
        sum += unit_amount(string_x[0])
        sum += 10 #for the "hundred and" part
        if(int(string_x[1]) == 1):
            sum += teen_amount(str(10 + int(string_x[2])))
        else:
            sum += unit_amount(string_x[2]) + tens_amount(string_x[1])
    else:
        sum += 11

print(sum)
        
