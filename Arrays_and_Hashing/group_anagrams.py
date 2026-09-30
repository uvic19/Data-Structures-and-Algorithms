"""
Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/

Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            output[tuple(count)].append(s)
            
        return list(output.values())

# --- Time & Space Complexity ---
# TC: O(m * n)
# SC: O(m * n)
