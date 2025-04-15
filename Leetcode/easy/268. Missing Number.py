class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #max_num=max(nums)
        hashset=set()
        for i in nums:
            hashset.add(i)
        for i in range(len(nums)+1):
            if i not in hashset:
                return i