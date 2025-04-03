# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         def partition(left,right):
#             pivot = nums[right]
#             p=left
#             for i in range(left,right):
#                 if nums[i]>pivot:
#                     nums[i],nums[p] = nums[p],nums[i]
#                     p+=1
#             nums[p],nums[right] = nums[right],nums[p]

#             return p
#         def quickSelect(left,right):
            
#             while left<=right:
#                 pivot = random.randint(left,right)
#                 nums[right],nums[pivot] = nums[pivot], nums[right]
#                 pivot_index = partition(left,right)

#                 if pivot_index == k-1:
#                     return nums[pivot_index]
#                 elif pivot_index<k-1:
#                     left=pivot_index+1
#                 elif pivot_index>k-1:
#                     right=pivot_index -1
#         return  quickSelect(0,len(nums)-1)
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

        heap =heap.nlargest(k,nums)
        return heap[-1]




                


        