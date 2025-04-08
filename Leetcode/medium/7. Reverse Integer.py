class Solution:
    def reverse(self, x: int) -> int:
        sign=False
        if x<0:
            sign =True
            x=x*(-1)

        x=int(str(x)[::-1])
        if x > 2**31 - 1:
            return 0

        return x*(-1) if sign else x    


        
