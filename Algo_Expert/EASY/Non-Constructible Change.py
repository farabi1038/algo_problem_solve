'''
Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're given no coins, the minimum amount of change that you can't create is 1
'''

#Solution:

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    #print(coins_sorted)
    min_value = 0
    for i in coins:
        if i >min_value + 1:
            return min_value + 1
        else :
            min_value = min_value + i
    return min_value + 1
            
            
        
    

    
        
