"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
Note: You may assume the string contains only lowercase English letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, c in enumerate(s):
            if c in seen:
                seen[c] = -1
            else:
                seen[c] = i

        for v in seen.values():
            if v != -1:
                return v

        return -1
