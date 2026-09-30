"""
Problem: 128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set()
        
        for n in nums:
            seen.add(n)
        
        streak = 0

        for n in seen:
            if n - 1 not in seen:
                start = n
                curr_streak = 1

                while n + 1 in seen:
                    n += 1
                    curr_streak += 1

                streak = max(streak,curr_streak)
            
        return streak
        

# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(n)
