# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         hashmap=defaultdict(int)
#         for i in nums:
#             hashmap[i]+=1
#         majority=len(nums)//2

#         for items,value in hashmap.items():
#             if value>majority:
#                 return items
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       return Counter(nums).most_common(1)[0][0]
        