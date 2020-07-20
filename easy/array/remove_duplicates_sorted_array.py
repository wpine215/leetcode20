"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that 
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

Lessons learned:
    - Always check list bounds
    - When iterating with an index offset, remember to account for it
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Counter also acts as a lagging cursor/index for in-place overwriting
        counter = 0
        cursor = 0

        # Skip last iteration to prevent index out of bounds
        while cursor < len(nums) - 1:
            cursor += 1

            # Increment if current number is not a repeat of previous
            if nums[cursor-1] < nums[cursor]:
                counter += 1

            # Perform in-place overwriting
            nums[counter] = nums[cursor]

        # Compensate for missed iteration above
        return counter + 1
