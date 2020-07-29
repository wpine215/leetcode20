"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1

        for c in t:
            if c in seen:
                seen[c] -= 1
                if seen[c] == 0:
                    seen.pop(c)
            else:
                return False

        if len(seen) > 0:
            return False
        return True
