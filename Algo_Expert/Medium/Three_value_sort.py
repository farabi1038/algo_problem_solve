#Three_value_sort

def threeNumberSort(array, order):
    # Write your code here.
    
    firstIdx=0
    thirdIdx =len(array)-1
    pointer=0
    for i in range (len(array)):
        if array[i]==order[0]:
            array[firstIdx],array[i] = array[i],array[firstIdx]
            firstIdx+=1
   
    for i in reversed(range (len(array))):
        if array[i]==order[2]:
            array[thirdIdx],array[i] = array[i],array[thirdIdx]
            thirdIdx-=1
    return array        