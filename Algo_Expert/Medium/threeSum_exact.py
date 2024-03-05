'''

Given an array of integers, find all triplets in the array that sum up to a given target value.

In other words, given an array arr and a target value target, return all triplets a, b, c such that a + b + c = target.

Example:

Input array: [7, 12, 3, 1, 2, -6, 5, -8, 6]
Target sum: 0

Output: [[2, -8, 6], [3, 5, -8], [1, -6, 5]]


'''



def threeNumberSum(array, targetSum):
    array.sort()
    res = []
    # Write your code here.
    for i in range (len(array)):
        lp = i+1
        rp = len(array)-1
        while lp<rp:
            
            cs = array[i] + array[lp] + array[rp]
            if cs == targetSum:
                print(i,lp,rp,"res")
                res.append([array[i],array[lp],array[rp]])
                lp = lp+1
                rp = rp-1
            elif cs < targetSum:
                lp = lp+1
            
            else:
                rp = rp-1
    return res


print(threeNumberSum([1, 2, 3], 7))