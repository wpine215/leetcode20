"""
https://leetcode.com/problems/climbing-stairs/submissions/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Lessons learned:
    - This is basically fibonacci. Requires recursion
    - Can "cache" recursive calls in a simple list that can be checked against first, before making additional recursive calls
    - Can build base case into the cache
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memoize = [0, 1, 2] + ([0] * (n - 2))
        return self.climbStairsRecursive(n, memoize)
    
    def climbStairsRecursive(self, n: int, map) -> int:
        if map[n] == 0:
            map[n] = self.climbStairsRecursive(n-1, map) + self.climbStairsRecursive(n-2, map)
        return map[n]
