def first_word( wordone, wordtwo):
    loopsone = len(wordone)
    loopstwo = len(wordtwo)
    if( loopsone > loopstwo):
        lessloops = loopstwo
    else:
        lessloops = loopsone

    for x in range(0,lessloops,1):
        if( ord(wordone[x]) > ord(wordtwo[x])):
            return wordtwo
        if( ord(wordone[x]) < ord(wordtwo[x])):
            return wordone
    if(loopsone<loopstwo):
        return wordone
    else:
        return wordtwo
        
#the method above works definitly..i think


#do a merge sort maybe...
#and get the aschii value of each word for stuff..
#
#
#
x = []
names = open("names#22.txt","r")
x = names.read().split(',')
names.close()




print(first_word("hello","hellos"))

print(len(x))
