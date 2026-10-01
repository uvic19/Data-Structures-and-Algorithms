"""
Problem: 739. Daily Temperatures
Link: https://leetcode.com/problems/daily-temperatures/

Description:
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        output = [0] * n

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_i = stack.pop()
                output[prev_i] = i - prev_i
            
            stack.append(i)
        
        return output

# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(n)
