"""
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Do not return anything, modify nums in-place instead.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes = 0
        write_index = 0

        for i, n in enumerate(nums):
            if n == 0:
                zeroes += 1 
            else:
                nums[write_index] = n
                write_index += 1

        offset = len(nums)-zeroes
        for i, n in enumerate(nums[offset:], offset):
            nums[i] = 0
