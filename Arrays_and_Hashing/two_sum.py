"""
Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/

Description:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            complement = target - value
            
            if complement in seen:
                return [index, seen[complement]]
            
            seen[value] = index

        
        
# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(n)
