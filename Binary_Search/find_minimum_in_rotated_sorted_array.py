"""
Problem: 153. Find Minimum in Rotated Sorted Array
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Description:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.
"""
from typing import List

class Solution:
    def findMin(self, nums: list[int]) -> int:
        L = 0
        R = len(nums) - 1
        
        while L < R:
            mid = (L + R) // 2

            if nums[mid] <= nums[R]:
                R = mid
            
            elif nums[mid] > nums[R]:
                L = mid + 1
        
        return nums[L]
            
        

# --- Time & Space Complexity ---
# TC: O(log n)
# SC: O(1)
