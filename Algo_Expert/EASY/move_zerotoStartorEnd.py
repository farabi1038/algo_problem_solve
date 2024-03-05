#move_zerotoStartorEnd



class Solution:
    #movezeros to right
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0  # This will keep track of the position to place the non-zero number.
        # Move all the non-zero numbers to the beginning of the array.
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1



def move_zeros_to_left(nums):
      #TODO: Write - Your - Code
      lastNonZeroFoundAt = len(nums) - 1
      # Move all non-zero numbers to the end of the array in reverse order.
      for i in reversed(range(len(nums))):  # Iterate in reverse to prioritize moving non-zeros to the end.
            if nums[i] != 0:
                nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt -= 1
