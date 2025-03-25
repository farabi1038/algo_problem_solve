class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        max_prof=0
        while right<len(prices):
            diff =prices[right] -prices[left]
            if diff<0:
                left=right
            else:
                max_prof=max(diff,max_prof)
            right+=1       
        return max_prof