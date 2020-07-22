"""
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice 
in the array, and it should return false if every element is distinct.

Lessons learned:
    - Initialize a set with set(), not {} (that's a dict)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False