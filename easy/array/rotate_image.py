"""
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise), in-place.

Lessons learned:
    - Always subtract 1 from len when indexing last element in list
    - When rotating 90 degrees at a time, the row index of one element becomes
      the column index of another, or vice-versa.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Iterate through layers of the matrix
        n = len(matrix)
        for i in range(n // 2):
            # Iterate through all digits in row of layer except last and rotate
            for j in range(i, n-i-1):
                first = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = first
