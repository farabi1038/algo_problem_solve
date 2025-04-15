class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        hashset=set(nums)
        print(hashset)
        length=0
        longest=0
        for n in hashset:
            if n-1 not in hashset:
                length =1
                while n+length in hashset:
                    length+=1
                longest=max(longest,length)
        return  longest           

        