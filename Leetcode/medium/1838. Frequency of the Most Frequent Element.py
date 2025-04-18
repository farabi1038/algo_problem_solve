class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        res = 0

        for right in range(len(nums)):
            # Add cost to bring all elements in window to nums[right]
            total += nums[right]

            # Check if current window is valid
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]
                left += 1

            # Update max frequency
            res = max(res, right - left + 1)

        return res
            