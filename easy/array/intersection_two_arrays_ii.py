"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Lessons learned:
    - Ask clarifying questions in interview
    - The solution is often simpler than you may think
    - In this case, order did not matter at all, which confused me at first
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        result = []
        
        # Place numbers from first array into dictionary
        for n in nums1:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        # Check 2nd array against dict, and subtract from count if matches
        for n in nums2:
            if n in count and count[n] > 0:
                count[n] -= 1
                result.append(n)
                
        return result
