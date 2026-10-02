"""
Problem: 33. Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Description:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length).
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4
"""
from typing import List

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid
            
            if nums[L] <= nums[mid]:

                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                
                else:
                    L = mid + 1
            
            else:

                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                
                else:
                    R = mid - 1
        
        return -1

# --- Time & Space Complexity ---
# TC: O(log n)
# SC: O(1)
