"""
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.
If reversed integer exceeds 2^31, return 0.

Lessons learned:
    - You can't use .reversed() on a string, use [::-1] instead!
"""


class Solution:
    def reverse(self, x: int) -> int:
        s_x = str(x)
        if x < 0:
            s_x = s_x[1:]

        s_x = s_x[::-1]

        if int(s_x) >= 2 ** 31:
            return 0
        if x < 0:
            return -1 * int(s_x)
        return int(s_x)
