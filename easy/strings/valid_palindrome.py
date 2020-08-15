"""
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Lessons learned:
    - Always account for edge cases if index exceeds list bounds
    - If indexing the last element, the index is len(list) - 1
    - If incrementing after an operation in a loop, keep in mind that you have
      to account for that extra increment while using the original value in that same iteration
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize indexes at beginning and end
        front_index = 0
        back_index = len(s) - 1
        
        while(True):
            # If we hit list boundaries, we're done here
            if back_index < 0 or front_index >= len(s):
                break

            # Initialize inner loop exit variables
            forward = False
            backward = False
            
            while not forward:
                # Keep iterating until we find alphanumeric char or reach end
                if s[front_index].isalnum() or front_index == len(s)-1:
                    forward = True
                front_index += 1
            
            while not backward:
                # Keep iterating until we find alphanumeric char or reach beginning
                if s[back_index].isalnum() or back_index == 0:
                    backward = True
                back_index -= 1
                
            # Check if pointers have collided/crossed over
            # Using -2 instead of 0 because we incremented/decremented above
            if back_index - front_index <= -2:
                break                
            
            # If alphanumeric characters in iteration don't match, return false
            if s[front_index-1].lower() != s[back_index+1].lower():
                return False
                   
        return True
