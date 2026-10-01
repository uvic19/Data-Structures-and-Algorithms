"""
Problem: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ')':'(', '}':'{',']':'[' }
        for c in s:
            if c in mapping:
                if not stack or stack[-1] != mapping[c]:
                    return False
                
                stack.pop()
            
            else:
                stack.append(c)
        
        return len(stack) == 0

# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(n)
