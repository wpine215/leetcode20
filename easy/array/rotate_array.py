"""
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.
Do not return anything, modify nums in-place instead.

Lessons learned:
    - If using a custom iterator variable, make sure to increment it
    - If using a custom iterator variable, make sure to check bounds 
        and wrap around to beginning, if the problem requires it
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        cache = []

        # Account for edge cases (including k > list length)
        if k % len(nums) == 0:
            return
        elif k > len(nums):
            k = k % len(nums)

        # Calculate the index to retrieve values from
        offset = len(nums) - k

        for i in range(len(nums)):
            if len(cache) < k:
                # Save the existing value, then overwrite it with the offset index's value
                cache.append(nums[i])
                nums[i] = nums[offset]
            else:
                # If the cache is full, read from that
                cache.append(nums[i])
                nums[i] = cache.pop(0)

            # If offset index reaches end, wrap around to beginning
            if offset == len(nums) - 1:
                offset = 0
            else:
                offset += 1
