"""
Problem: 238. Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        output = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output

# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(1)
