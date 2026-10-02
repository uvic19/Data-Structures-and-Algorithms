"""
Problem: 704. Binary Search
Link: https://leetcode.com/problems/binary-search/

Description:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.
"""
from typing import List

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        L = 0
        R = n - 1

        while L <= R:
            mid = (L + R) // 2

            if target == nums[mid]:
                return mid
            
            elif target < nums[mid]:
                R = mid - 1
            
            elif target > nums[mid]:
                L = mid + 1
            
        return -1
# --- Time & Space Complexity ---
# TC: O(log n)
# SC: O(1)
