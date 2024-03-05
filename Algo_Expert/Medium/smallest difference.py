def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    pointer =0
    pointer2=0
    smallest = 100000000
    index1=0
    index2=0
    # print(arrayOne)
    # print(arrayTwo)
    while pointer<len(arrayOne) and pointer2<len(arrayTwo):
        diff= abs(arrayOne[pointer] - arrayTwo[pointer2])
        #print(diff,arrayOne[pointer],arrayTwo[pointer2],pointer,pointer2)
        if abs(diff) < smallest :
            smallest = diff
            index1 = arrayOne[pointer]
            index2 = arrayTwo[pointer2]    
            
            
        elif arrayOne[pointer] < arrayTwo[pointer2] :
            pointer =pointer +1
        else :
            pointer2 =pointer2 +1
            
            
    return [index1,index2]    


    
print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))