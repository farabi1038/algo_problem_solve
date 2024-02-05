#Single_cycle_check

def hasSingleCycle(array):
    # Write your code here.
    elmCount=0
    idxCount=0
    while elmCount<len(array):
        elmCount+=1
        idxCount+=array[idxCount]
        idxCount=idxCount%len(array)
        if idxCount<0:
            idxCount+=len(array)
        if (idxCount==0 and elmCount!=len(array)) or (idxCount!=0 and elmCount==len(array)):
            return False
    return True        
        
