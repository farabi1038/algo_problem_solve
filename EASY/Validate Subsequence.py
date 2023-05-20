'''
Validate Subsequence
Understanding the problem
We are given two arrays of integers array and sequence. We are asked to implement a function that is going to check whether all the numbers in the sequence appear in the array and they appear in the same order. In other words, the function needs to find out if we can get the sequence array from the array, when we delete some or no elements in the array without changing the order of the remaining elements.

Example:

array: [3, 1, 7, 5, 10, 2];
sequence: [1, 5, 2];
Output: true
'''

def isValidSubsequence(array, sequence):
    # Write your code here.
    j=0
    for i in array:
        if i==sequence[j]:
            j=j+1
        if j==len(sequence):
         return True
    return False 