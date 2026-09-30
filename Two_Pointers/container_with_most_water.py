"""
Problem: 11. Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/

Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
"""
from typing import List

class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        max_area = 0

        L, R = 0, n - 1

        while L < R:    
            area = (R - L) * min(height[L],height[R])
            max_area = max(max_area, area)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return max_area

# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(1)
