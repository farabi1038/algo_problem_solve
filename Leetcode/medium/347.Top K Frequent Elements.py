from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n for n,m in Counter(nums).most_common(k)]


# from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = Counter(nums)
#         common=freq.most_common(k)
#         return [n for n,m in common ]


# from collections import Counter
# import heapq

# def topKFrequent(nums, k):
#     freq = Counter(nums)  # Step 1: Count frequencies
#     return heapq.nlargest(k, freq.keys(), key=freq.get)  # Step 2: Get top-k
