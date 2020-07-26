"""
https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Lessons learned:
    - zip(*my2Dlist) is an easy way to transpose a 2D list/matrix
    - A list of sets must be created using a list comprehension:
        - list_of_sets = [set() for i in range(num)]
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for n in row:
                if n == ".":
                    continue
                if int(n) not in seen:
                    seen.add(int(n))
                elif int(n) in seen:
                    return False
           
        for col in zip(*board):
            seen = set()
            for n in col:
                if n == ".":
                    continue
                if int(n) not in seen:
                    seen.add(int(n))
                elif int(n) in seen:
                    return False
 
        seen = [set() for i in range(9)]
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                idx = (i//3) + 3*(j//3)
                if n == ".":
                    continue
                if int(n) not in seen[idx]:
                    seen[idx].add(int(n))
                elif int(n) in seen[idx]:
                    return False

        return True
