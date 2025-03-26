class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=nums[0]
        temp_sum =nums[0]
        for i in range (1,len(nums)):
            temp_sum= max(temp_sum+nums[i],nums[i])
            curr_sum=max(curr_sum,temp_sum)
        return   curr_sum  

        
