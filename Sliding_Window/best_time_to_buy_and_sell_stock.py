"""
Problem: 121. Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        L = 0
        R = 1
        while R < len(prices):

            if prices[L] > prices[R]:
                L = R
            else:
                profit = prices[R] - prices[L]
                max_profit = max(max_profit,profit)

            R += 1
        
        return max_profit
        

# --- Time & Space Complexity ---
# TC: O(n)
# SC: O(1)
