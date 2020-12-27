##def copyArray(arrayOrig, arrayNew):
##    length = len(arrayOrig)
##    for x in range(0,length-1,1):
##        arrayNew[x] = arrayOrig[x]
##        
##def swap(array,a, b):
##    c = array[b]
##    array[b] = array[a]
##    array[a] = c
##
##
##pandArray = [1,2,3,4]
##restore = [1,2,3,4]
##z = len(pandArray)-1
##y = z - 1
##
##for a in range(0,4,1):
##    for b in range(0,3,1):
##        for c in range(0,2,1):
##            for d in range(0,1,1):
##                print(pandArray)
##                swap(pandArray, z, y)
##                print(pandArray)

## figured out another way, but i really want to be able to cycle through every pandigital number...:(

array_of_poss = [102]
works = False
for x in range(119,999,17):
    array_of_poss.append(x)
    
for y in range(0,len(array_of_poss)-1, 1):
    for d in range (13, 3, -2):
        for z in range(1,9,1):
            addMult = (z*(11-((d+1)/2)))
            print(array_of_poss)
            if( addMult + (array_of_poss[y]//(10*(8-((d+1)/2))))%d == 0):
                works = True
                array_of_poss[y].insert(addMult + array_of_poss[y])
                array_of_poss.
                print(array_of_poss)
                break
        if(works==False):
            array_of_poss.remove(y)
            y = y-1
        else:
            break
    works = False

                
print (array_of_poss)


































    
    
    
