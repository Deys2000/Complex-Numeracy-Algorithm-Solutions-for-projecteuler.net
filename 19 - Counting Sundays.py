def next_month( today, month,year):
    if(month%12 == 4 or month%12 == 6 or month%12 == 9 or month%12 == 11):
        today += 30
    elif(month%12 == 1 or month%12 == 3 or month%12 == 5 or month%12 == 7 or month%12 == 8 or month%12 == 10 or month%12 == 12):
        today += 31
    else:
        today+= 28
        if(year%4==0):
            today+=1
    return today

sun_on_month = 0
this_day = 1
for month in range(1,12*100,1):
    this_day += next_month(this_day, month, (month//12))
    if(this_day%7 == 6):
        sun_on_month +=1
print(sun_on_month)

# i got 172, high probability of it being wrong just because it is the first try
    
