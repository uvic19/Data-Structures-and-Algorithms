"""
Problem: 15. 3Sum
Link: https://leetcode.com/problems/3sum/

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        n = len(nums)

        nums.sort()

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i + 1, n - 1

            while L < R:

                curr_sum = nums[i] + nums[L] + nums[R]

                if curr_sum > 0:
                    R -= 1

                elif curr_sum < 0:
                    L += 1

                else:
                    output.append([nums[i], nums[L], nums[R]])

                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

        return output

# --- Time & Space Complexity ---
# TC: O(n^2)
# SC: O(n)
