"""
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Lessons learned:
    - Always allocate a temporary variable if swapping two or more variables in-place
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            temp = s[n-i-1]
            s[n-i-1] = s[i]
            s[i] = temp
