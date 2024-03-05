
'''
Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, 
if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. 
Expected time complexity is O(n) and extra space is O(1).

'''



def moveElementToEnd(array, toMove):
    # Write your code here.
    pointerL = 0
    pointerR = len(array)-1
    element_move=0
    while pointerL<pointerR:
        if array[pointerR] != toMove:
            if array[pointerL] == toMove:
                array[pointerR], array[pointerL] = array[pointerL], array[pointerR]
                pointerR = pointerR-1 #miised this line and error
            pointerL = pointerL + 1
        else:
            pointerR = pointerR-1
    
    return array
             
            

             
            
print(moveElementToEnd([2, 4, 2, 5, 6, 2, 2],2))