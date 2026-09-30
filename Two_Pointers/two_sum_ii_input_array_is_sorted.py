"""
Problem: 167. Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Description:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        
        L, R = 0, n - 1

        while L < R:
            curr_sum = numbers[L] + numbers[R]
            
            if curr_sum > target:
                R -= 1
            elif curr_sum < target:
                L += 1
            else:
                return [L + 1, R + 1]

        

# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(1)
