"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Could you implement it without using extra memory?

Lessons learned:
    - Remember your bitwise operations and their properties (like XOR in this case).
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result = result ^ n
        return result
