
'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise
'''



def isMonotonic(array):
    # Write your code here.
    boolI=True
    boolD=True
    if len(array)==0 or len(array)==1:
        return True
    for i in range (len(array)):
        if i+1<len(array):
            if array[i]> array[i+1]:
                boolI =False
            if array[i]< array[i+1]:
                boolD =False
    if boolD == False and boolI== False:
        return False
    else:
        return True
                
        
        
