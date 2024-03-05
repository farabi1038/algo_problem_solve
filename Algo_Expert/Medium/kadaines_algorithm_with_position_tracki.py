#kadaines_algorithm_with_position_tracking


def kadanesAlgorithm(array):
    # Write your code here.
    sum =array[0]
    currentSum=array[0]
    idxS=0
    idxN=1
    temp=0
    for i in range(1,len(array)):
        if array[i]>sum+array[i]:
            sum = array[i]
            temp = idxS
            
        else:
            temp=i
            sum =array[i]+sum
            
        if sum>currentSum:
            currentSum=sum
            indxS=temp
            idxN= i
            
    return currentSum        
            
            
    
