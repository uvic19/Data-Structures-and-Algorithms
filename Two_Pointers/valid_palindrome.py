"""
Problem: 125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/

Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Given a string s, return true if it is a palindrome, or false otherwise.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        L, R = 0, n - 1

        while L < R:

            if not s[L].isalnum():
                L += 1
                continue
            
            if not s[R].isalnum():
                R -= 1
                continue
            
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
    
        return True 
               

# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(1)
