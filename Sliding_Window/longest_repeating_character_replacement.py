"""
Problem: 424. Longest Repeating Character Replacement
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Description:
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        L = 0
        max_f = 0
        max_l = 0

        for R in range(len(s)):
            if s[R] not in seen:
                seen[s[R]] = 1
            else:
                seen[s[R]] += 1
        
            max_f = max(max_f,seen[s[R]])

            if (R - L + 1) - max_f > k:
                seen[s[L]] -= 1
                L += 1
            
            max_l = max(max_l, R - L + 1)
        
        return max_l
# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(m)  # where m is 26 (uppercase English letters), which simplifies to O(1)
