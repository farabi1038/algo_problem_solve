class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sorted_list = []
        count = 0
        for num in reversed(nums):
            # Count elements less than num / 2
            count += bisect.bisect_left(sorted_list, num / 2)
            # Insert current number in sorted order
            bisect.insort(sorted_list, num)
        return count
        # seen = []
        # count = 0
        # for num in reversed(nums):
        #     for val in seen:  # linear scan
        #         if val < num / 2:
        #             count += 1
        #     seen.append(num)
        # return count
