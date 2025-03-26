class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        three = n//3
        reminder = n%3

        if reminder ==1:
            three=three-1
            reminder =4
        if reminder ==0:
            reminder =1
        return (3**three)*reminder    
            
        