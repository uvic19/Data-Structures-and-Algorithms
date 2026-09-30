"""
Problem: 3. Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Description:
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = 0
        max_len = 0

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            
            seen.add(s[R])
            max_len = max(max_len, R - L + 1)
        
        return max_len


# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(m)  # where m is the character set size (e.g. 128 for ASCII), which simplifies to O(1)
