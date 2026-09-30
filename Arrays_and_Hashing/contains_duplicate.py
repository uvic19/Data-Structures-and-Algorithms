"""
Problem: 217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Description:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(n)
